#!/usr/bin/env python3
"""Document ingestion pipeline for the Presales AI Platform RAG system.

Reads all knowledge files and indexes them into a local ChromaDB vector
database using Ollama nomic-embed-text embeddings.
"""

import argparse
import logging
import os
import sys
from pathlib import Path
from typing import Optional

import chromadb
import pdfplumber
import requests
from docx import Document
from dotenv import load_dotenv
from rich.console import Console
from rich.progress import Progress
from rich.table import Table

load_dotenv()

logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO"),
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)
console = Console()


def get_embedding(text: str, model: str, base_url: str) -> list:
    """Generate an embedding vector via the Ollama embeddings API.

    Args:
        text: Input text to embed.
        model: Ollama model name (e.g. nomic-embed-text).
        base_url: Ollama API base URL (e.g. http://localhost:11434).

    Returns:
        Embedding as a list of floats.

    Raises:
        ConnectionError: If Ollama is not reachable.
        ValueError: If the API response is malformed or returns an error.
    """
    url = f"{base_url.rstrip('/')}/api/embeddings"
    try:
        response = requests.post(
            url,
            json={"model": model, "prompt": text},
            timeout=60,
        )
        response.raise_for_status()
        data = response.json()
        return data["embedding"]
    except requests.exceptions.ConnectionError as e:
        raise ConnectionError(
            f"Cannot connect to Ollama at {base_url}. "
            "Ensure Ollama is running: ollama serve"
        ) from e
    except requests.exceptions.HTTPError as e:
        raise ValueError(f"Ollama API returned an error: {e}") from e
    except KeyError as e:
        raise ValueError(f"Unexpected Ollama response format — missing key: {e}") from e


def chunk_text(text: str, chunk_size: int = 400, overlap: int = 50) -> list:
    """Split text into overlapping word-count chunks.

    Args:
        text: Input text to split.
        chunk_size: Target word count per chunk.
        overlap: Word count overlap between consecutive chunks.

    Returns:
        List of chunk strings. Chunks with fewer than 50 words are skipped.
    """
    words = text.split()
    if not words:
        return []

    step = max(1, chunk_size - overlap)
    chunks = []
    start = 0

    while start < len(words):
        end = min(start + chunk_size, len(words))
        chunk_words = words[start:end]
        if len(chunk_words) >= 50:
            chunks.append(" ".join(chunk_words))
        start += step

    return chunks


def index_markdown_file(
    file_path: str,
    collection: chromadb.Collection,
    doc_type: str,
    base_url: str,
) -> int:
    """Index a markdown file into ChromaDB.

    Reads the file, skips files containing placeholder content ('[ADD:'),
    chunks the text, generates embeddings, and upserts all chunks with
    metadata.

    Args:
        file_path: Path to the markdown file.
        collection: ChromaDB collection to write into.
        doc_type: Document category: 'product', 'industry', or 'proposal'.
        base_url: Ollama API base URL.

    Returns:
        Number of chunks indexed. Returns 0 if the file was skipped.
    """
    model = os.getenv("OLLAMA_EMBEDDING_MODEL", "nomic-embed-text:latest")
    path = Path(file_path)

    try:
        content = path.read_text(encoding="utf-8")
    except OSError as e:
        logger.warning("Cannot read %s: %s", path.name, e)
        return 0

    if "[ADD:" in content:
        logger.info("Skipping %s — contains placeholder content", path.name)
        return 0

    chunks = chunk_text(content)
    if not chunks:
        logger.warning("No usable chunks extracted from %s", path.name)
        return 0

    indexed = 0
    for i, chunk in enumerate(chunks):
        try:
            embedding = get_embedding(chunk, model, base_url)
        except (ConnectionError, ValueError) as e:
            logger.error("Embedding failed for chunk %d of %s: %s", i, path.name, e)
            continue

        collection.upsert(
            ids=[f"{path.name}__chunk_{i}"],
            embeddings=[embedding],
            documents=[chunk],
            metadatas=[{
                "source_file": path.name,
                "doc_type": doc_type,
                "chunk_index": i,
                "full_path": str(path.resolve()),
            }],
        )
        indexed += 1

    logger.debug("Indexed %d chunks from %s", indexed, path.name)
    return indexed


def index_docx_file(
    file_path: str,
    collection: chromadb.Collection,
    base_url: str,
) -> int:
    """Index a Word document into ChromaDB.

    Extracts all paragraph text, chunks it, generates embeddings, and
    upserts chunks with doc_type='proposal'.

    Args:
        file_path: Path to the .docx file.
        collection: ChromaDB collection to write into.
        base_url: Ollama API base URL.

    Returns:
        Number of chunks indexed. Returns 0 if the file was skipped or
        unreadable.
    """
    model = os.getenv("OLLAMA_EMBEDDING_MODEL", "nomic-embed-text:latest")
    path = Path(file_path)

    try:
        doc = Document(str(path))
    except Exception as e:
        logger.warning("Cannot read Word document %s: %s", path.name, e)
        return 0

    paragraphs = [p.text.strip() for p in doc.paragraphs if p.text.strip()]
    content = "\n".join(paragraphs)

    if "[ADD:" in content:
        logger.info("Skipping %s — contains placeholder content", path.name)
        return 0

    chunks = chunk_text(content)
    if not chunks:
        logger.warning("No usable chunks extracted from %s", path.name)
        return 0

    indexed = 0
    for i, chunk in enumerate(chunks):
        try:
            embedding = get_embedding(chunk, model, base_url)
        except (ConnectionError, ValueError) as e:
            logger.error("Embedding failed for chunk %d of %s: %s", i, path.name, e)
            continue

        collection.upsert(
            ids=[f"{path.name}__chunk_{i}"],
            embeddings=[embedding],
            documents=[chunk],
            metadatas=[{
                "source_file": path.name,
                "doc_type": "proposal",
                "chunk_index": i,
                "full_path": str(path.resolve()),
            }],
        )
        indexed += 1

    logger.debug("Indexed %d chunks from %s", indexed, path.name)
    return indexed


def _index_pdf_file(
    file_path: str,
    collection: chromadb.Collection,
    base_url: str,
) -> int:
    """Index a PDF file into ChromaDB using pdfplumber for text extraction.

    Args:
        file_path: Path to the PDF file.
        collection: ChromaDB collection to write into.
        base_url: Ollama API base URL.

    Returns:
        Number of chunks indexed. Returns 0 if the file was skipped or
        unreadable.
    """
    model = os.getenv("OLLAMA_EMBEDDING_MODEL", "nomic-embed-text:latest")
    path = Path(file_path)

    try:
        with pdfplumber.open(str(path)) as pdf:
            page_texts = [page.extract_text() or "" for page in pdf.pages]
        content = "\n".join(page_texts).strip()
    except Exception as e:
        logger.warning("Cannot read PDF %s: %s", path.name, e)
        return 0

    if not content:
        logger.warning("No text extracted from PDF %s", path.name)
        return 0

    if "[ADD:" in content:
        logger.info("Skipping %s — contains placeholder content", path.name)
        return 0

    chunks = chunk_text(content)
    if not chunks:
        logger.warning("No usable chunks extracted from %s", path.name)
        return 0

    indexed = 0
    for i, chunk in enumerate(chunks):
        try:
            embedding = get_embedding(chunk, model, base_url)
        except (ConnectionError, ValueError) as e:
            logger.error("Embedding failed for chunk %d of %s: %s", i, path.name, e)
            continue

        collection.upsert(
            ids=[f"{path.name}__chunk_{i}"],
            embeddings=[embedding],
            documents=[chunk],
            metadatas=[{
                "source_file": path.name,
                "doc_type": "proposal",
                "chunk_index": i,
                "full_path": str(path.resolve()),
            }],
        )
        indexed += 1

    logger.debug("Indexed %d chunks from %s", indexed, path.name)
    return indexed


def index_all_documents(
    knowledge_dir: str,
    chroma_dir: str,
    base_url: str,
    rebuild: bool = False,
) -> dict:
    """Index all knowledge documents into ChromaDB.

    Scans knowledge/products/, knowledge/industries/, and
    knowledge/proposals/ for .md, .docx, and .pdf files and indexes
    each into the 'presales_knowledge' ChromaDB collection.

    Args:
        knowledge_dir: Path to the knowledge base root directory.
        chroma_dir: Path where ChromaDB will persist its data.
        base_url: Ollama API base URL.
        rebuild: If True, deletes the existing collection before indexing.

    Returns:
        Summary dict with keys: products, industries, proposals,
        total_chunks, skipped.
    """
    client = chromadb.PersistentClient(path=chroma_dir)
    collection_name = "presales_knowledge"

    if rebuild:
        try:
            client.delete_collection(name=collection_name)
            logger.info("Deleted existing collection '%s'", collection_name)
            console.print(
                f"[yellow]Deleted existing collection '{collection_name}'[/yellow]"
            )
        except Exception:
            logger.debug("No existing collection '%s' to delete", collection_name)

    collection = client.get_or_create_collection(
        name=collection_name,
        metadata={"hnsw:space": "cosine"},
    )
    logger.info(
        "Using ChromaDB collection '%s' at %s", collection_name, chroma_dir
    )

    knowledge_path = Path(knowledge_dir)
    summary: dict = {
        "products": 0,
        "industries": 0,
        "proposals": 0,
        "total_chunks": 0,
        "skipped": 0,
    }

    scan_dirs = [
        (knowledge_path / "products", "product", "products"),
        (knowledge_path / "industries", "industry", "industries"),
        (knowledge_path / "proposals", "proposal", "proposals"),
    ]

    with Progress(console=console) as progress:
        for folder, doc_type, summary_key in scan_dirs:
            if not folder.exists():
                logger.warning("Knowledge directory not found: %s", folder)
                continue

            supported_files = sorted([
                f for f in folder.iterdir()
                if f.is_file()
                and f.suffix.lower() in {".md", ".docx", ".pdf"}
                and not f.name.startswith(".")
                and f.name != ".gitkeep"
            ])

            if not supported_files:
                logger.info("No supported files in %s", folder)
                continue

            task = progress.add_task(
                f"[cyan]Indexing {folder.name}[/cyan]",
                total=len(supported_files),
            )

            for file_path in supported_files:
                suffix = file_path.suffix.lower()
                chunks = 0

                if suffix == ".md":
                    chunks = index_markdown_file(
                        str(file_path), collection, doc_type, base_url
                    )
                elif suffix == ".docx":
                    chunks = index_docx_file(str(file_path), collection, base_url)
                elif suffix == ".pdf":
                    chunks = _index_pdf_file(str(file_path), collection, base_url)

                if chunks == 0:
                    summary["skipped"] += 1
                else:
                    summary[summary_key] += chunks
                    summary["total_chunks"] += chunks

                progress.advance(task)

    logger.info(
        "Indexing complete — products: %d, industries: %d, proposals: %d, "
        "total: %d, skipped: %d",
        summary["products"],
        summary["industries"],
        summary["proposals"],
        summary["total_chunks"],
        summary["skipped"],
    )
    return summary


def main() -> None:
    """CLI entry point for document indexing.

    Usage:
        python src/rag/indexer.py --rebuild   # Delete and rebuild entire index
        python src/rag/indexer.py --update    # Add new documents only (upsert)
        python src/rag/indexer.py             # Defaults to --update behaviour
    """
    parser = argparse.ArgumentParser(
        description="Index knowledge documents into ChromaDB for RAG retrieval"
    )
    parser.add_argument(
        "--rebuild",
        action="store_true",
        help="Delete existing index and rebuild from scratch",
    )
    parser.add_argument(
        "--update",
        action="store_true",
        help="Add/update documents without deleting existing index (default)",
    )
    args = parser.parse_args()

    knowledge_dir = os.getenv("KNOWLEDGE_DIR", "knowledge")
    chroma_dir = os.getenv("CHROMA_DB_DIR", "chroma_db")
    base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    rebuild = args.rebuild

    mode_label = "Rebuilding" if rebuild else "Updating"
    console.print(f"\n[bold blue]{mode_label} knowledge index[/bold blue]")
    console.print(f"  Knowledge dir : {knowledge_dir}")
    console.print(f"  ChromaDB dir  : {chroma_dir}")
    console.print(f"  Ollama URL    : {base_url}\n")

    try:
        summary = index_all_documents(
            knowledge_dir=knowledge_dir,
            chroma_dir=chroma_dir,
            base_url=base_url,
            rebuild=rebuild,
        )
    except ConnectionError as e:
        console.print(f"[bold red]Connection error:[/bold red] {e}")
        sys.exit(1)

    table = Table(
        title="Indexing Summary",
        show_header=True,
        header_style="bold cyan",
    )
    table.add_column("Category", style="cyan")
    table.add_column("Chunks Indexed", justify="right", style="green")

    table.add_row("Product docs", str(summary["products"]))
    table.add_row("Industry docs", str(summary["industries"]))
    table.add_row("Proposal docs", str(summary["proposals"]))
    table.add_row("[bold]Total chunks[/bold]", f"[bold]{summary['total_chunks']}[/bold]")
    table.add_row("Skipped files", str(summary["skipped"]))

    console.print(table)


if __name__ == "__main__":
    main()
