"""PDF text extraction module for the Presales AI Platform."""

import logging
from pathlib import Path
from typing import Any

import pdfplumber

logger = logging.getLogger(__name__)


def extract_pdf_text(file_path: str) -> dict[str, Any]:
    """Extract text content from a PDF file, page by page.

    Args:
        file_path: Absolute or relative path to the PDF file.

    Returns:
        A dict with keys:
            - file_name (str): Basename of the PDF.
            - page_count (int): Total number of pages.
            - word_count (int): Total word count across all pages.
            - full_text (str): Concatenated text from all pages.
            - pages (list[dict]): Per-page dicts with 'page' (1-based int) and 'text' (str).

    Raises:
        FileNotFoundError: If the file does not exist at file_path.
        ValueError: If the file extension is not .pdf.
    """
    path = Path(file_path)

    if not path.exists():
        logger.error("PDF file not found: %s", file_path)
        raise FileNotFoundError(f"PDF file not found: {file_path}")

    if path.suffix.lower() != ".pdf":
        logger.error("Invalid file type '%s'; expected .pdf", path.suffix)
        raise ValueError(f"Expected a .pdf file, got: '{path.suffix}'")

    logger.info("Extracting text from: %s", file_path)

    pages_data: list[dict[str, Any]] = []
    scanned_page_count = 0

    with pdfplumber.open(file_path) as pdf:
        total_pages = len(pdf.pages)
        logger.info("PDF has %d pages", total_pages)

        for i, page in enumerate(pdf.pages, start=1):
            text = page.extract_text() or ""
            if not text.strip():
                scanned_page_count += 1
                logger.debug(
                    "Page %d appears empty or scanned (no text extracted)", i
                )
            pages_data.append({"page": i, "text": text})

    if scanned_page_count > 0:
        pct = scanned_page_count / total_pages * 100
        logger.warning(
            "%d/%d pages (%.0f%%) yielded no extractable text — PDF may contain "
            "scanned images. Consider running OCR for complete extraction.",
            scanned_page_count,
            total_pages,
            pct,
        )

    full_text = "\n\n".join(p["text"] for p in pages_data)
    word_count = len(full_text.split())

    logger.info("Extraction complete: %d pages, %d words", total_pages, word_count)

    return {
        "file_name": path.name,
        "page_count": total_pages,
        "word_count": word_count,
        "full_text": full_text,
        "pages": pages_data,
    }
