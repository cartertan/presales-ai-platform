"""Interactive product selection menu for the Presales AI Platform."""

import logging
import sys
from pathlib import Path
from typing import Any

import yaml
from rich import box
from rich.console import Console
from rich.table import Table

logger = logging.getLogger(__name__)
console = Console()

_DEFAULT_CONFIG_PATH = Path(__file__).parent.parent / "config" / "products.yaml"


def load_products(config_path: str) -> list[dict[str, Any]]:
    """Load product definitions from a YAML config file.

    Args:
        config_path: Absolute or relative path to the products YAML file.

    Returns:
        List of product dicts, each with keys: id, name, short, category,
        description.

    Raises:
        FileNotFoundError: If the config file does not exist.
        yaml.YAMLError: If the YAML cannot be parsed.
    """
    path = Path(config_path)
    if not path.exists():
        raise FileNotFoundError(f"Products config not found: {path}")
    with open(path, encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    products: list[dict[str, Any]] = data.get("products", [])
    logger.info("Loaded %d products from %s", len(products), path)
    return products


def _fallback_select(
    products: list[dict[str, Any]], choices: list[str]
) -> list[dict[str, Any]]:
    """Numbered fallback input for environments without questionary.

    Renders a numbered list and reads a comma-separated input string from stdin.
    Re-prompts until at least one valid product is selected.

    Args:
        products: Full product list in the same order as choices.
        choices: Formatted display strings for each product.

    Returns:
        List of selected product dicts.
    """
    console.print("\n[bold blue]Available Nexus Products:[/bold blue]")
    for i, choice in enumerate(choices, start=1):
        console.print(f"  [dim]{i:>2}.[/dim] {choice}")

    while True:
        try:
            raw = input("\nEnter product numbers separated by commas (e.g. 1,3,5): ").strip()
        except (EOFError, KeyboardInterrupt):
            console.print("\n[yellow]Selection cancelled.[/yellow]")
            sys.exit(0)

        parts = [p.strip() for p in raw.split(",") if p.strip()]
        indices: list[int] = []
        valid = True
        for part in parts:
            if not part.isdigit() or not (1 <= int(part) <= len(choices)):
                console.print(f"[red]Invalid selection: '{part}' — enter numbers 1–{len(choices)}[/red]")
                valid = False
                break
            indices.append(int(part) - 1)

        if not valid:
            continue
        if not indices:
            console.print("[yellow]Please select at least one product.[/yellow]")
            continue

        return [products[i] for i in indices]


def select_products() -> list[dict[str, Any]]:
    """Present an interactive product selection menu.

    Attempts to use questionary.checkbox for a rich terminal experience.
    Falls back to numbered input if questionary is unavailable.

    Guarantees at least one product is returned; re-prompts if the user
    submits an empty selection.

    Returns:
        List of selected product dicts (id, name, short, category, description).
    """
    products = load_products(str(_DEFAULT_CONFIG_PATH))
    choices = [
        f"[{p['id']:>2}] {p['name']} ({p['category']}) — {p['description']}"
        for p in products
    ]

    try:
        import questionary  # noqa: PLC0415

        console.print(
            "\n[bold blue]Select Nexus products to include in this proposal:[/bold blue]"
        )
        selected_labels: list[str] | None = questionary.checkbox(
            "SPACE to select / deselect — ENTER to confirm:",
            choices=choices,
        ).ask()

        if selected_labels is None:
            # User pressed Ctrl-C inside questionary
            console.print("\n[yellow]Selection cancelled.[/yellow]")
            sys.exit(0)

        if not selected_labels:
            console.print("[yellow]No products selected. Please select at least one.[/yellow]")
            return select_products()

        selected = [p for label, p in zip(choices, products) if label in selected_labels]

    except ImportError:
        logger.warning("questionary not available — using numbered input fallback.")
        selected = _fallback_select(products, choices)

    logger.info(
        "Selected %d product(s): %s", len(selected), [p["name"] for p in selected]
    )
    return selected


def display_selected(products: list[dict[str, Any]]) -> None:
    """Render a Rich table summarising the selected products.

    Args:
        products: List of selected product dicts to display.
    """
    table = Table(
        title="[bold green]Selected Products for Proposal[/bold green]",
        box=box.ROUNDED,
        border_style="green",
        show_lines=True,
    )
    table.add_column("#", style="dim", width=4, justify="right")
    table.add_column("Product Name", style="bold cyan")
    table.add_column("Category", style="yellow")
    table.add_column("Code", style="dim", justify="center", width=8)

    for p in products:
        table.add_row(
            str(p.get("id", "")),
            p.get("name", ""),
            p.get("category", ""),
            p.get("short", ""),
        )

    console.print()
    console.print(table)
