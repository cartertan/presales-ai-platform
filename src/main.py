"""CLI entry point for the Presales AI Platform — Phase 1 pipeline."""

import argparse
import json
import logging
import os
import sys
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv
from rich import box
from rich.console import Console
from rich.logging import RichHandler
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn, TimeElapsedColumn
from rich.table import Table

from analyzer import (
    ANALYSIS_MODEL,
    FALLBACK_MODEL,
    OLLAMA_BASE_URL,
    analyze_rfp,
    check_ollama,
)
from compliance import generate_excel
from extractor import extract_pdf_text

load_dotenv()

console = Console()

_DEFAULT_OUTPUT_DIR = os.getenv("OUTPUT_DIR", "output")
_OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
_ANALYSIS_MODEL = os.getenv("OLLAMA_ANALYSIS_MODEL", "qwq:latest")


def _setup_logging(log_level: str) -> None:
    """Configure root logger to use Rich handler.

    Args:
        log_level: One of DEBUG, INFO, WARNING, ERROR.
    """
    level = getattr(logging, log_level.upper(), logging.INFO)
    logging.basicConfig(
        level=level,
        format="%(message)s",
        handlers=[
            RichHandler(
                console=console,
                rich_tracebacks=True,
                show_time=True,
                show_path=False,
            )
        ],
    )


def _parse_args() -> argparse.Namespace:
    """Parse and return CLI arguments."""
    parser = argparse.ArgumentParser(
        prog="presales-ai",
        description="Presales AI Platform — transforms RFP PDFs into presales artefacts",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  python src/main.py --rfp data/rfp/tender.pdf\n"
            "  python src/main.py --rfp data/rfp/tender.pdf --phase 1 --output results/\n"
        ),
    )
    parser.add_argument(
        "--rfp",
        required=True,
        metavar="PATH",
        help="Path to the RFP PDF file",
    )
    parser.add_argument(
        "--phase",
        type=int,
        default=1,
        choices=[1],
        metavar="N",
        help="Pipeline phase to run (default: 1)",
    )
    parser.add_argument(
        "--output",
        default=_DEFAULT_OUTPUT_DIR,
        metavar="DIR",
        help=f"Output directory (default: {_DEFAULT_OUTPUT_DIR})",
    )
    parser.add_argument(
        "--log-level",
        default=os.getenv("LOG_LEVEL", "INFO"),
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        help="Log verbosity (default: INFO)",
    )
    return parser.parse_args()


def _print_banner() -> None:
    """Render the application banner to the console."""
    console.print(
        Panel.fit(
            "[bold blue]Presales AI Platform[/bold blue]\n"
            "[dim]RFP  →  Compliance Matrix    Phase 1[/dim]",
            border_style="blue",
        )
    )
    console.print()


def _abort(message: str) -> None:
    """Print an error panel and exit with code 1.

    Args:
        message: Human-readable error description.
    """
    console.print(
        Panel(
            f"[bold red]{message}[/bold red]",
            title="[red]Error[/red]",
            border_style="red",
        )
    )
    sys.exit(1)


def _check_ollama_or_abort(base_url: str) -> None:
    """Verify Ollama is reachable; call _abort() if not.

    Args:
        base_url: Ollama API base URL to probe.
    """
    if not check_ollama(base_url):
        console.print(
            Panel(
                f"[bold]Cannot connect to Ollama at[/bold] [yellow]{base_url}[/yellow]\n\n"
                "Make sure Ollama is running:\n"
                "  [bold green]ollama serve[/bold green]\n\n"
                "Then retry.",
                title="[red]Ollama Unreachable[/red]",
                border_style="red",
            )
        )
        sys.exit(1)


def _print_outputs_table(outputs: list[dict[str, str]]) -> None:
    """Render a summary table of all pipeline outputs.

    Args:
        outputs: List of dicts with keys 'step', 'output', 'status'.
    """
    table = Table(
        title="[bold green]Pipeline Complete — Generated Outputs[/bold green]",
        box=box.ROUNDED,
        border_style="green",
        show_lines=True,
    )
    table.add_column("Step", style="cyan", no_wrap=True, min_width=22)
    table.add_column("Output / Details", style="white")
    table.add_column("Status", justify="center", min_width=8)

    for item in outputs:
        table.add_row(item["step"], item["output"], item["status"])

    console.print(table)


def run_phase1(rfp_path: str, output_dir: str) -> int:
    """Execute Phase 1: extract → analyse → generate compliance Excel.

    Args:
        rfp_path: Path to the RFP PDF file.
        output_dir: Directory for all output artefacts.

    Returns:
        0 on success, 1 on any failure.
    """
    logger = logging.getLogger(__name__)
    outputs: list[dict[str, str]] = []

    _check_ollama_or_abort(_OLLAMA_BASE_URL)
    console.print(
        f"[green]Ollama reachable[/green] at [dim]{_OLLAMA_BASE_URL}[/dim]  "
        f"| Analysis model: [bold]{_ANALYSIS_MODEL}[/bold]  "
        f"| Fallback: [dim]{FALLBACK_MODEL}[/dim]"
    )
    console.print()

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        TimeElapsedColumn(),
        console=console,
        transient=False,
    ) as progress:

        # ── Step 1: Extract PDF ──────────────────────────────────────────────
        task1 = progress.add_task(
            "[cyan]Step 1/3  Extracting PDF text…", total=None
        )
        try:
            extraction = extract_pdf_text(rfp_path)
        except FileNotFoundError as exc:
            progress.stop()
            _abort(str(exc))
        except ValueError as exc:
            progress.stop()
            _abort(str(exc))

        progress.update(
            task1,
            description=(
                f"[green]Step 1/3  PDF extracted[/green]  "
                f"({extraction['page_count']} pages, "
                f"{extraction['word_count']:,} words)"
            ),
        )
        outputs.append({
            "step": "1. PDF Extraction",
            "output": (
                f"{extraction['file_name']} — "
                f"{extraction['page_count']} pages, "
                f"{extraction['word_count']:,} words"
            ),
            "status": "[green]Done[/green]",
        })

        # ── Step 2: Analyse with Ollama ──────────────────────────────────────
        task2 = progress.add_task(
            f"[cyan]Step 2/3  Analysing RFP with {_ANALYSIS_MODEL}…", total=None
        )
        analyzer_config = {
            "base_url": _OLLAMA_BASE_URL,
            "analysis_model": _ANALYSIS_MODEL,
            "timeout": 300,
        }
        try:
            analysis = analyze_rfp(extraction["full_text"], analyzer_config)
        except (RuntimeError, ValueError) as exc:
            progress.stop()
            _abort(f"RFP analysis failed: {exc}")

        analysis["_rfp_filename"] = extraction["file_name"]
        req_count = len(analysis.get("requirements", []))
        model_used = analysis.get("_model_used", _ANALYSIS_MODEL)

        progress.update(
            task2,
            description=(
                f"[green]Step 2/3  Analysis complete[/green]  "
                f"({req_count} requirements, model: {model_used})"
            ),
        )
        outputs.append({
            "step": "2. RFP Analysis",
            "output": (
                f"{req_count} requirements extracted  |  "
                f"Industry: {analysis.get('industry_vertical', 'Unknown')}  |  "
                f"Model: {model_used}"
            ),
            "status": "[green]Done[/green]",
        })

        # Save analysis JSON for use by later phases
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        stem = Path(rfp_path).stem[:20]
        date_str = datetime.now().strftime("%Y%m%d")
        json_path = Path(output_dir) / f"{stem}_analysis_{date_str}.json"
        try:
            with open(json_path, "w", encoding="utf-8") as fh:
                json.dump(analysis, fh, indent=2, ensure_ascii=False)
            logger.info("Analysis JSON saved: %s", json_path)
            outputs.append({
                "step": "2b. Analysis JSON",
                "output": str(json_path.resolve()),
                "status": "[green]Saved[/green]",
            })
        except OSError as exc:
            logger.warning("Could not save analysis JSON: %s", exc)

        # ── Step 3: Generate Compliance Matrix Excel ─────────────────────────
        task3 = progress.add_task(
            "[cyan]Step 3/3  Generating Compliance Matrix Excel…", total=None
        )
        try:
            excel_path = generate_excel(analysis, output_dir)
        except OSError as exc:
            progress.stop()
            _abort(f"Excel generation failed: {exc}")

        progress.update(
            task3,
            description="[green]Step 3/3  Compliance Matrix Excel created[/green]",
        )
        outputs.append({
            "step": "3. Compliance Matrix",
            "output": excel_path,
            "status": "[green]Done[/green]",
        })

    console.print()
    _print_outputs_table(outputs)
    return 0


def main() -> None:
    """Parse arguments, configure logging, and dispatch to the requested phase."""
    args = _parse_args()
    _setup_logging(args.log_level)
    _print_banner()

    if args.phase == 1:
        exit_code = run_phase1(args.rfp, args.output)
    else:
        console.print(f"[yellow]Phase {args.phase} is not yet implemented.[/yellow]")
        exit_code = 1

    sys.exit(exit_code)


if __name__ == "__main__":
    main()
