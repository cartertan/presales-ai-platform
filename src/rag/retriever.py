#!/usr/bin/env python3
"""Semantic search retriever for the Presales AI Platform RAG system.

Queries the ChromaDB knowledge base built by indexer.py using Ollama
nomic-embed-text embeddings for similarity search.
"""

import logging
import os
from typing import Optional

import chromadb
import requests
from dotenv import load_dotenv
from rich.console import Console
from rich.table import Table

load_dotenv()

logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO"),
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)
console = Console()


def get_query_embedding(query: str, model: str, base_url: str) -> list:
    """Generate an embedding vector for a search query via Ollama.

    Args:
        query: Search query text.
        model: Ollama embedding model name (e.g. nomic-embed-text).
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
            json={"model": model, "prompt": query},
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


def search_knowledge(
    query: str,
    n_results: int = 5,
    doc_type: Optional[str] = None,
    chroma_dir: str = "chroma_db",
    base_url: str = "http://localhost:11434",
) -> list:
    """Search the knowledge base using semantic similarity.

    Opens the ChromaDB 'presales_knowledge' collection, embeds the query,
    and returns the closest matching chunks optionally filtered by doc_type.

    Args:
        query: Natural language search query.
        n_results: Number of results to return.
        doc_type: Optional filter — 'product', 'industry', or 'proposal'.
        chroma_dir: Path to ChromaDB persistent storage directory.
        base_url: Ollama API base URL.

    Returns:
        List of result dicts with keys: text, source, doc_type,
        chunk_index, distance.

    Raises:
        RuntimeError: If ChromaDB collection is not found (run indexer first).
        ConnectionError: If Ollama is not reachable.
        ValueError: If the embedding API response is malformed.
    """
    model = os.getenv("OLLAMA_EMBEDDING_MODEL", "nomic-embed-text:latest")
    collection_name = "presales_knowledge"

    try:
        client = chromadb.PersistentClient(path=chroma_dir)
        collection = client.get_collection(name=collection_name)
    except Exception as e:
        raise RuntimeError(
            f"Knowledge base not found at '{chroma_dir}'. "
            "Run the indexer first: python src/rag/indexer.py --rebuild"
        ) from e

    embedding = get_query_embedding(query, model, base_url)

    count = collection.count()
    if count == 0:
        logger.warning("Knowledge base is empty — run the indexer first")
        return []

    safe_n = min(n_results, count)

    query_kwargs: dict = {
        "query_embeddings": [embedding],
        "n_results": safe_n,
        "include": ["documents", "metadatas", "distances"],
    }
    if doc_type:
        query_kwargs["where"] = {"doc_type": doc_type}

    try:
        results = collection.query(**query_kwargs)
    except Exception as e:
        logger.error("ChromaDB query failed: %s", e)
        raise RuntimeError(f"Search query failed: {e}") from e

    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]
    distances = results.get("distances", [[]])[0]

    output = []
    for doc, meta, dist in zip(documents, metadatas, distances):
        output.append({
            "text": doc,
            "source": meta.get("source_file", "unknown"),
            "doc_type": meta.get("doc_type", "unknown"),
            "chunk_index": meta.get("chunk_index", 0),
            "distance": dist,
        })

    logger.debug("Query '%s' returned %d results", query, len(output))
    return output


def search_products(
    query: str,
    n_results: int = 3,
    base_url: str = "http://localhost:11434",
) -> list:
    """Search product knowledge documents only.

    Args:
        query: Natural language search query.
        n_results: Number of results to return.
        base_url: Ollama API base URL.

    Returns:
        List of result dicts (same schema as search_knowledge).
    """
    chroma_dir = os.getenv("CHROMA_DB_DIR", "chroma_db")
    return search_knowledge(
        query=query,
        n_results=n_results,
        doc_type="product",
        chroma_dir=chroma_dir,
        base_url=base_url,
    )


def search_industries(
    query: str,
    n_results: int = 2,
    base_url: str = "http://localhost:11434",
) -> list:
    """Search industry knowledge documents only.

    Args:
        query: Natural language search query.
        n_results: Number of results to return.
        base_url: Ollama API base URL.

    Returns:
        List of result dicts (same schema as search_knowledge).
    """
    chroma_dir = os.getenv("CHROMA_DB_DIR", "chroma_db")
    return search_knowledge(
        query=query,
        n_results=n_results,
        doc_type="industry",
        chroma_dir=chroma_dir,
        base_url=base_url,
    )


def search_proposals(
    query: str,
    n_results: int = 3,
    base_url: str = "http://localhost:11434",
) -> list:
    """Search past proposal documents only.

    Args:
        query: Natural language search query.
        n_results: Number of results to return.
        base_url: Ollama API base URL.

    Returns:
        List of result dicts (same schema as search_knowledge).
    """
    chroma_dir = os.getenv("CHROMA_DB_DIR", "chroma_db")
    return search_knowledge(
        query=query,
        n_results=n_results,
        doc_type="proposal",
        chroma_dir=chroma_dir,
        base_url=base_url,
    )


def format_context(results: list, max_chars: int = 3000) -> str:
    """Format search results into a context string for LLM prompt injection.

    Each result is rendered as:
        SOURCE: <filename>
        CONTENT: <chunk text>
        ---

    The full output is truncated at max_chars characters.

    Args:
        results: List of result dicts from search_knowledge.
        max_chars: Maximum character length of the returned string.

    Returns:
        Formatted multi-source context string ready for LLM injection.
    """
    parts = []
    for result in results:
        block = (
            f"SOURCE: {result['source']}\n"
            f"CONTENT: {result['text']}\n"
            "---"
        )
        parts.append(block)

    context = "\n".join(parts)
    if len(context) > max_chars:
        context = context[:max_chars]
    return context


def test_retrieval() -> None:
    """Run 3 verification queries to confirm RAG is working correctly.

    Queries:
        1. certificate lifecycle management PKI
        2. government national identity eID
        3. V2G charging ISO 15118 Plug and Charge

    Prints a result table for each query to the console. Used to verify
    that the index is populated and embeddings are returning sensible matches.
    """
    base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    chroma_dir = os.getenv("CHROMA_DB_DIR", "chroma_db")

    test_queries = [
        "certificate lifecycle management PKI",
        "government national identity eID",
        "V2G charging ISO 15118 Plug and Charge",
    ]

    console.print("\n[bold blue]RAG Retrieval Test[/bold blue]\n")

    for query in test_queries:
        console.print(f"[bold cyan]Query:[/bold cyan] {query}")

        try:
            results = search_knowledge(
                query=query,
                n_results=3,
                chroma_dir=chroma_dir,
                base_url=base_url,
            )
        except RuntimeError as e:
            console.print(f"[red]Error:[/red] {e}\n")
            continue
        except (ConnectionError, ValueError) as e:
            console.print(f"[red]Error:[/red] {e}\n")
            continue

        if not results:
            console.print("[yellow]No results found.[/yellow]\n")
            continue

        table = Table(show_header=True, header_style="bold", expand=False)
        table.add_column("Source", style="cyan", max_width=35)
        table.add_column("Type", style="magenta", max_width=10)
        table.add_column("Distance", justify="right", max_width=10)
        table.add_column("Preview", max_width=60)

        for result in results:
            preview = result["text"][:120].replace("\n", " ")
            table.add_row(
                result["source"],
                result["doc_type"],
                f"{result['distance']:.4f}",
                preview,
            )

        console.print(table)
        console.print()


if __name__ == "__main__":
    test_retrieval()
