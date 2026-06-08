"""Word document generator: creates a professional customer summary from RFP analysis."""

import json
import logging
import os
import re
from datetime import datetime
from pathlib import Path
from typing import Any

import requests
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt, RGBColor
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

SUMMARY_MODEL = os.getenv("OLLAMA_SUMMARY_MODEL", "qwen3.6:27b")
SUMMARY_FALLBACK = os.getenv("OLLAMA_SUMMARY_FALLBACK", "qwq:latest")
SUMMARY_FALLBACK_2 = os.getenv("OLLAMA_SUMMARY_FALLBACK_2", "granite4.1:30b")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

_DARK_BLUE = RGBColor(0x1F, 0x38, 0x64)
_WHITE = RGBColor(0xFF, 0xFF, 0xFF)
_GREY_TEXT = RGBColor(0x60, 0x60, 0x60)
_TABLE_HEADER_HEX = "1F3864"
_ALT_ROW_HEX = "EEF2F7"


# ── XML / OOXML helpers ───────────────────────────────────────────────────────

def _shade_cell(cell: Any, hex_color: str) -> None:
    """Set the background fill of a table cell via OOXML.

    Args:
        cell: python-docx TableCell object.
        hex_color: Six-character hex string without '#', e.g. "1F3864".
    """
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    for existing in tcPr.findall(qn("w:shd")):
        tcPr.remove(existing)
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hex_color)
    tcPr.append(shd)


def _append_field_code(para: Any, field_instr: str) -> None:
    """Append a Word field-code run (PAGE, NUMPAGES, etc.) to a paragraph.

    Args:
        para: python-docx Paragraph to append to.
        field_instr: Field instruction, e.g. "PAGE" or "NUMPAGES".
    """
    run = para.add_run()
    run.font.size = Pt(9)

    begin = OxmlElement("w:fldChar")
    begin.set(qn("w:fldCharType"), "begin")
    run._r.append(begin)

    instr_elem = OxmlElement("w:instrText")
    instr_elem.set(qn("xml:space"), "preserve")
    instr_elem.text = f" {field_instr} "
    run._r.append(instr_elem)

    sep = OxmlElement("w:fldChar")
    sep.set(qn("w:fldCharType"), "separate")
    run._r.append(sep)

    end_elem = OxmlElement("w:fldChar")
    end_elem.set(qn("w:fldCharType"), "end")
    run._r.append(end_elem)


def _add_page_numbers(doc: Document) -> None:
    """Insert 'Page X of Y' field codes in the document footer.

    Args:
        doc: The python-docx Document to modify.
    """
    section = doc.sections[0]
    footer = section.footer
    para = footer.paragraphs[0] if footer.paragraphs else footer.add_paragraph()
    para.clear()
    para.alignment = WD_ALIGN_PARAGRAPH.CENTER

    pre = para.add_run("Page ")
    pre.font.size = Pt(9)
    _append_field_code(para, "PAGE")
    mid = para.add_run(" of ")
    mid.font.size = Pt(9)
    _append_field_code(para, "NUMPAGES")


# ── Document structure builders ───────────────────────────────────────────────

def _add_title_page(
    doc: Document, customer_name: str, project_title: str, display_date: str
) -> None:
    """Create a formatted title page with a trailing page break.

    Args:
        doc: Document to append to.
        customer_name: Organisation or customer name.
        project_title: RFP or project title.
        display_date: Human-readable date string, e.g. "8 June 2026".
    """
    for _ in range(7):
        doc.add_paragraph()

    brand = doc.add_paragraph()
    brand.alignment = WD_ALIGN_PARAGRAPH.CENTER
    br = brand.add_run("NEXUS GROUP")
    br.font.color.rgb = _DARK_BLUE
    br.font.size = Pt(11)
    br.bold = True
    br.font.all_caps = True

    doc.add_paragraph()

    title_para = doc.add_paragraph()
    title_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    tr = title_para.add_run(project_title)
    tr.font.color.rgb = _DARK_BLUE
    tr.font.size = Pt(26)
    tr.bold = True

    subtitle_para = doc.add_paragraph()
    subtitle_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    sr = subtitle_para.add_run("Customer Summary & RFP Analysis")
    sr.font.color.rgb = _DARK_BLUE
    sr.font.size = Pt(16)

    doc.add_paragraph()

    for label, value in [("Prepared for", customer_name), ("Date", display_date)]:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(f"{label}:  {value}")
        r.font.size = Pt(12)

    doc.add_paragraph()

    conf_para = doc.add_paragraph()
    conf_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cr = conf_para.add_run("CONFIDENTIAL — FOR INTERNAL USE ONLY")
    cr.font.size = Pt(9)
    cr.font.color.rgb = _GREY_TEXT
    cr.italic = True

    doc.add_page_break()


def _add_heading(doc: Document, text: str, level: int = 1) -> Any:
    """Add a dark blue heading paragraph.

    Args:
        doc: Document to append to.
        text: Heading text.
        level: Heading level (1 or 2).

    Returns:
        The created Paragraph.
    """
    para = doc.add_paragraph(style=f"Heading {level}")
    run = para.add_run(text)
    run.font.color.rgb = _DARK_BLUE
    run.bold = True
    run.font.size = Pt(14 if level == 1 else 12)
    return para


def _create_styled_table(doc: Document, headers: list[str]) -> Any:
    """Create a bordered table with a dark blue header row.

    Args:
        doc: Document to append to.
        headers: Column header labels.

    Returns:
        The created Table (header row already populated).
    """
    table = doc.add_table(rows=1, cols=len(headers))
    table.style = "Table Grid"
    hdr_row = table.rows[0]
    for cell, header in zip(hdr_row.cells, headers):
        _shade_cell(cell, _TABLE_HEADER_HEX)
        cell.paragraphs[0].clear()
        run = cell.paragraphs[0].add_run(header)
        run.font.color.rgb = _WHITE
        run.bold = True
        run.font.size = Pt(10)
    return table


def _add_table_row(
    table: Any, values: list[str], shading: str | None = None
) -> None:
    """Append a data row to a table.

    Args:
        table: python-docx Table to append to.
        values: Cell values for the new row.
        shading: Optional hex colour for the row background.
    """
    row = table.add_row()
    for cell, value in zip(row.cells, values):
        cell.text = str(value)
        if shading:
            _shade_cell(cell, shading)
        for para in cell.paragraphs:
            para.alignment = WD_ALIGN_PARAGRAPH.LEFT


def _add_bullet_list(doc: Document, items: list[str]) -> None:
    """Render a list of strings as 'List Bullet' paragraphs.

    Args:
        doc: Document to append to.
        items: Text lines; leading bullet markers are stripped.
    """
    for item in items:
        clean = re.sub(r"^[\•\-\*\–]\s*", "", item.strip())
        if clean:
            doc.add_paragraph(clean, style="List Bullet")


def _add_numbered_list(doc: Document, items: list[str]) -> None:
    """Render a list of strings as 'List Number' paragraphs.

    Args:
        doc: Document to append to.
        items: Text lines; leading number markers are stripped.
    """
    for item in items:
        clean = re.sub(r"^\d+[\.\)]\s*", "", item.strip())
        if clean:
            doc.add_paragraph(clean, style="List Number")


# ── Context and model helpers ─────────────────────────────────────────────────

def _build_context(
    analysis: dict[str, Any], keys: list[str], max_chars: int = 6000
) -> str:
    """Concatenate selected analysis fields into a compact context string.

    Args:
        analysis: Full RFP analysis dict.
        keys: Keys to include.
        max_chars: Maximum character length before truncation.

    Returns:
        Formatted context string ready to pass to the model.
    """
    parts: list[str] = []
    for key in keys:
        value = analysis.get(key)
        if value:
            label = key.upper().replace("_", " ")
            parts.append(f"{label}:\n{json.dumps(value, indent=2, ensure_ascii=False)}")
    text = "\n\n".join(parts)
    if len(text) > max_chars:
        text = text[:max_chars] + "\n[context truncated]"
    return text


def _extract_json_list(raw: str) -> list[dict[str, Any]] | None:
    """Attempt to parse a JSON array from raw model output.

    Tries direct parse, markdown-fence strip, then bracket search.

    Args:
        raw: Raw text potentially containing a JSON array.

    Returns:
        Parsed list, or None if all parse attempts fail.
    """
    for candidate in [
        raw,
        re.sub(r"```(?:json)?", "", raw).strip(),
    ]:
        try:
            result = json.loads(candidate)
            if isinstance(result, list):
                return result
        except json.JSONDecodeError:
            pass

    start, end = raw.find("["), raw.rfind("]")
    if start != -1 and end > start:
        try:
            result = json.loads(raw[start : end + 1])
            if isinstance(result, list):
                return result
        except json.JSONDecodeError:
            pass

    return None


def generate_section(prompt: str, context: str, model: str, base_url: str) -> str:
    """Generate text for one document section using Ollama.

    Calls `model` first; falls back to SUMMARY_FALLBACK ("qwq:latest") then
    SUMMARY_FALLBACK_2 ("granite4.1:30b") if prior models fail.

    Args:
        prompt: Instruction describing what to generate for this section.
        context: Supporting context extracted from the RFP analysis.
        model: Ollama model name to attempt first (e.g. "qwen3.6:27b").
        base_url: Ollama API base URL.

    Returns:
        Generated text stripped of leading/trailing whitespace.

    Raises:
        requests.exceptions.RequestException: If both primary and fallback fail.
    """
    payload: dict[str, Any] = {
        "model": model,
        "prompt": f"{prompt}\n\nContext:\n{context}",
        "stream": False,
        "options": {"temperature": 0.3, "num_predict": 2048},
    }

    def _call(m: str) -> str:
        p = {**payload, "model": m}
        logger.info("Calling Ollama model '%s' for section generation", m)
        resp = requests.post(f"{base_url}/api/generate", json=p, timeout=300)
        resp.raise_for_status()
        return resp.json().get("response", "").strip()

    try:
        return _call(model)
    except requests.exceptions.RequestException as exc:
        logger.warning(
            "Model '%s' failed (%s). Falling back to '%s'.", model, exc, SUMMARY_FALLBACK
        )
        try:
            return _call(SUMMARY_FALLBACK)
        except requests.exceptions.RequestException as exc2:
            logger.warning(
                "Model '%s' failed (%s). Falling back to '%s'.",
                SUMMARY_FALLBACK, exc2, SUMMARY_FALLBACK_2,
            )
            return _call(SUMMARY_FALLBACK_2)


# ── Per-section builders ──────────────────────────────────────────────────────

def _section1_rfp_overview(
    doc: Document,
    analysis: dict[str, Any],
    selected_products: list[dict[str, Any]],
) -> None:
    """Add Section 1: RFP Overview as a two-column table."""
    _add_heading(doc, "1. RFP Overview")

    requirements = analysis.get("requirements", [])
    mandatory = sum(
        1 for r in requirements if str(r.get("type", "")).upper() == "MANDATORY"
    )
    optional = len(requirements) - mandatory

    rfp_name = analysis.get("_rfp_filename", "Unknown")
    customer_name = Path(rfp_name).stem.replace("_", " ").replace("-", " ").title()

    product_names = (
        ", ".join(p.get("name", "") for p in selected_products)
        if selected_products
        else "TBC — to be selected"
    )

    table = _create_styled_table(doc, ["Field", "Value"])
    rows = [
        ("Customer / Organisation", customer_name),
        ("Project Title", rfp_name),
        ("Industry Vertical", analysis.get("industry_vertical") or "Not specified"),
        ("Submission Deadline", analysis.get("submission_deadline") or "Not specified"),
        ("Budget Range", analysis.get("budget") or "Not specified"),
        (
            "Requirements",
            f"{len(requirements)} total  —  {mandatory} Mandatory, {optional} Optional",
        ),
        ("Proposed Nexus Products", product_names),
    ]
    for i, (field, value) in enumerate(rows):
        _add_table_row(table, [field, value], _ALT_ROW_HEX if i % 2 == 0 else None)

    doc.add_paragraph()


def _section2_customer_objectives(
    doc: Document, analysis: dict[str, Any], model: str, base_url: str
) -> None:
    """Add Section 2: Customer Objectives as a model-generated bullet list."""
    _add_heading(doc, "2. Customer Objectives")

    context = _build_context(
        analysis, ["executive_summary", "customer_objectives", "win_themes"]
    )
    prompt = (
        "Based on the RFP analysis, write exactly 5 to 7 bullet points describing "
        "what the customer wants to achieve and the strategic goals behind this procurement.\n"
        "Return ONLY the bullet points, one per line, each starting with '• '.\n"
        "No headings, no preamble, no closing remarks."
    )
    raw = generate_section(prompt, context, model, base_url)
    lines = [ln.strip() for ln in raw.splitlines() if ln.strip()]
    _add_bullet_list(doc, lines[:8])
    doc.add_paragraph()


def _section3_use_cases(
    doc: Document, analysis: dict[str, Any], model: str, base_url: str
) -> None:
    """Add Section 3: Identified Use Cases as a model-generated numbered list."""
    _add_heading(doc, "3. Identified Use Cases")

    mandatory_sample = [
        r for r in analysis.get("requirements", [])
        if str(r.get("type", "")).upper() == "MANDATORY"
    ][:20]
    context = _build_context(
        {**analysis, "mandatory_requirements_sample": mandatory_sample},
        ["executive_summary", "mandatory_requirements_sample"],
    )
    prompt = (
        "Based on the RFP, identify 4 to 7 specific use cases the proposed solution must address.\n"
        "Format as a numbered list: '1. Use Case Name: One-paragraph description.'\n"
        "Return ONLY the numbered list. No headings, preamble, or closing remarks."
    )
    raw = generate_section(prompt, context, model, base_url)
    lines = [ln.strip() for ln in raw.splitlines() if ln.strip()]
    _add_numbered_list(doc, lines[:10])
    doc.add_paragraph()


def _section4_technical_requirements(
    doc: Document, analysis: dict[str, Any], model: str, base_url: str
) -> None:
    """Add Section 4: Technical Requirements Summary as a categorised table."""
    _add_heading(doc, "4. Technical Requirements Summary")

    reqs_json = json.dumps(analysis.get("requirements", [])[:30], indent=2, ensure_ascii=False)
    prompt = (
        "Categorise the RFP requirements into these categories: "
        "PKI, Authentication, Integration, Scalability, Security, Compliance, HA/DR.\n"
        "For each relevant category, summarise the key requirements and give a priority "
        "(High, Medium, or Low).\n"
        "Return ONLY a valid JSON array — no other text:\n"
        '[{"category": "PKI", "key_requirements": "summary text", "priority": "High"}]\n'
        "Omit categories with no relevant requirements."
    )
    raw = generate_section(prompt, f"REQUIREMENTS:\n{reqs_json}", model, base_url)

    items = _extract_json_list(raw)
    table = _create_styled_table(doc, ["Category", "Key Requirements", "Priority"])

    if items:
        for i, item in enumerate(items):
            _add_table_row(
                table,
                [
                    item.get("category", ""),
                    item.get("key_requirements", ""),
                    item.get("priority", ""),
                ],
                _ALT_ROW_HEX if i % 2 == 0 else None,
            )
    else:
        logger.warning("Section 4: JSON parse failed; inserting raw text.")
        _add_table_row(table, ["All categories", raw[:600], "TBC"])

    doc.add_paragraph()


def _section5_commercial_requirements(
    doc: Document, analysis: dict[str, Any], model: str, base_url: str
) -> None:
    """Add Section 5: Commercial Requirements as a model-generated bullet list."""
    _add_heading(doc, "5. Commercial Requirements")

    commercial_keywords = [
        "sla", "support", "training", "maintenance", "license",
        "timeline", "warranty", "commercial", "contract", "pricing",
    ]
    commercial_reqs = [
        r for r in analysis.get("requirements", [])
        if any(
            kw in (r.get("requirement", "") + r.get("section", "")).lower()
            for kw in commercial_keywords
        )
    ][:15]

    context = _build_context(
        {**analysis, "commercial_requirements": commercial_reqs},
        ["commercial_requirements", "budget"],
    )
    if not context.strip():
        context = _build_context(analysis, ["executive_summary"], max_chars=4000)

    prompt = (
        "Summarise the commercial requirements from this RFP covering these specific areas: "
        "SLA requirements, support and maintenance, training requirements, "
        "project timeline expectations, and licensing model.\n"
        "Write each topic as a bullet: '• Topic: Description.'\n"
        "Return ONLY the bullet points. No headings, preamble, or closing remarks."
    )
    raw = generate_section(prompt, context, model, base_url)
    lines = [ln.strip() for ln in raw.splitlines() if ln.strip()]
    _add_bullet_list(doc, lines[:10])
    doc.add_paragraph()


def _section6_evaluation_criteria(
    doc: Document, analysis: dict[str, Any], model: str, base_url: str
) -> None:
    """Add Section 6: Evaluation Criteria as a table with model-generated commentary."""
    _add_heading(doc, "6. Evaluation Criteria")

    criteria = analysis.get("evaluation_criteria", [])
    table = _create_styled_table(doc, ["Criterion", "Weight", "What It Means for Us"])

    if criteria:
        context = _build_context(analysis, ["evaluation_criteria", "win_themes"])
        prompt = (
            "For each evaluation criterion in the context, write one concise sentence "
            "explaining what it means strategically for a Nexus Group presales response.\n"
            "Return ONLY a JSON array matching this structure (same order as input criteria):\n"
            '[{"criterion": "...", "means": "one sentence"}]\n'
            "No other text."
        )
        raw = generate_section(prompt, context, model, base_url)
        meanings = _extract_json_list(raw) or []
        meanings_map = {m.get("criterion", ""): m.get("means", "") for m in meanings}

        for i, crit in enumerate(criteria):
            name = crit.get("criterion", "")
            _add_table_row(
                table,
                [name, crit.get("weight", ""), meanings_map.get(name, "")],
                _ALT_ROW_HEX if i % 2 == 0 else None,
            )
    else:
        _add_table_row(table, ["Not specified", "—", "—"])

    doc.add_paragraph()


def _section7_risks_and_gaps(
    doc: Document, analysis: dict[str, Any], model: str, base_url: str
) -> None:
    """Add Section 7: Key Risks and Gaps as a model-generated risk table."""
    _add_heading(doc, "7. Key Risks and Gaps")

    risk_reqs = [r for r in analysis.get("requirements", []) if r.get("risk_flag")][:15]
    context = _build_context(
        {**analysis, "flagged_requirements": risk_reqs},
        ["risk_areas", "flagged_requirements"],
    )
    prompt = (
        "Based on the risk areas and flagged requirements, identify the key risks, "
        "ambiguous requirements, missing information, and compliance gaps.\n"
        "Return ONLY a valid JSON array — no other text:\n"
        '[{"risk": "description", "severity": "High", "action": "recommended action"}]\n'
        "severity must be exactly one of: High, Medium, Low."
    )
    raw = generate_section(prompt, context, model, base_url)

    _severity_colour = {"High": "FFD7D7", "Medium": "FFF3CD", "Low": "D4EDDA"}
    items = _extract_json_list(raw)
    table = _create_styled_table(doc, ["Risk / Gap", "Severity", "Recommended Action"])

    if items:
        for item in items:
            severity = item.get("severity", "Medium")
            row = table.add_row()
            for cell, value in zip(
                row.cells,
                [item.get("risk", ""), severity, item.get("action", "")],
            ):
                cell.text = str(value)
                for para in cell.paragraphs:
                    para.alignment = WD_ALIGN_PARAGRAPH.LEFT
            _shade_cell(row.cells[1], _severity_colour.get(severity, _ALT_ROW_HEX))
    else:
        logger.warning("Section 7: JSON parse failed; inserting raw text.")
        _add_table_row(table, ["See analysis notes", "TBC", raw[:400]])

    doc.add_paragraph()


def _section8_clarification_questions(
    doc: Document, analysis: dict[str, Any], model: str, base_url: str
) -> None:
    """Add Section 8: Clarification Questions as a model-generated numbered list."""
    _add_heading(doc, "8. Clarification Questions")

    risk_reqs = [r for r in analysis.get("requirements", []) if r.get("risk_flag")][:15]
    gap_reqs = [r for r in analysis.get("requirements", []) if not r.get("nexus_solution")][:10]
    context = _build_context(
        {**analysis, "flagged_requirements": risk_reqs, "gap_requirements": gap_reqs},
        ["risk_areas", "flagged_requirements", "gap_requirements"],
    )
    prompt = (
        "Generate 6 to 8 clarification questions to ask the customer before submitting.\n"
        "Focus on ambiguous requirements, missing specifications, and technical gaps.\n"
        "Format each question as:\n"
        "'1. [Question text]\nRationale: [One sentence explaining why we need this.]'\n"
        "Return ONLY the numbered list. No headings, preamble, or closing remarks."
    )
    raw = generate_section(prompt, context, model, base_url)
    lines = [ln.strip() for ln in raw.splitlines() if ln.strip()]
    _add_numbered_list(doc, lines[:20])
    doc.add_paragraph()


# ── Public API ────────────────────────────────────────────────────────────────

def generate_summary(
    analysis: dict[str, Any], config: dict[str, Any], output_dir: str
) -> str:
    """Generate a professional customer summary Word document from RFP analysis.

    Creates a .docx with a title page and 8 sections. Sections 2–8 call the
    qwen3.6:27b Ollama model (fallbacks: qwq:latest → granite4.1:30b) for content generation.

    File saved to: output_dir/summaries/{rfp_stem}_Summary_{YYYYMMDD}.docx

    Args:
        analysis: Structured dict from analyzer.analyze_rfp(), must include
            a '_rfp_filename' key (set by main.py after analysis).
        config: Runtime configuration:
            - base_url (str): Ollama API base URL.
            - summary_model (str, optional): Override for the generation model.
            - selected_products (list[dict], optional): Products chosen in
              the product selector to include in Section 1.
        output_dir: Root output directory; summaries/ subdirectory is created.

    Returns:
        Absolute path to the saved .docx file.

    Raises:
        OSError: If the output directory cannot be created or the file cannot
            be written.
    """
    base_url = config.get("base_url", OLLAMA_BASE_URL)
    model = config.get("summary_model", SUMMARY_MODEL)
    selected_products: list[dict[str, Any]] = config.get("selected_products", [])

    summaries_dir = Path(output_dir) / "summaries"
    try:
        summaries_dir.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        logger.error("Cannot create summaries directory '%s': %s", summaries_dir, exc)
        raise

    rfp_name = analysis.get("_rfp_filename", "rfp")
    stem = Path(rfp_name).stem
    customer_name = stem.replace("_", " ").replace("-", " ").title()
    date_str = datetime.now().strftime("%Y%m%d")
    display_date = datetime.now().strftime("%d %B %Y")

    filename = f"{stem[:30]}_Summary_{date_str}.docx"
    file_path = summaries_dir / filename

    logger.info("Generating customer summary document: %s", file_path)

    doc = Document()
    _add_page_numbers(doc)
    _add_title_page(doc, customer_name, customer_name, display_date)

    logger.info("Section 1: RFP Overview")
    _section1_rfp_overview(doc, analysis, selected_products)

    logger.info("Section 2: Customer Objectives (model generation)")
    _section2_customer_objectives(doc, analysis, model, base_url)

    logger.info("Section 3: Identified Use Cases (model generation)")
    _section3_use_cases(doc, analysis, model, base_url)

    logger.info("Section 4: Technical Requirements Summary (model generation)")
    _section4_technical_requirements(doc, analysis, model, base_url)

    logger.info("Section 5: Commercial Requirements (model generation)")
    _section5_commercial_requirements(doc, analysis, model, base_url)

    logger.info("Section 6: Evaluation Criteria (model generation)")
    _section6_evaluation_criteria(doc, analysis, model, base_url)

    logger.info("Section 7: Key Risks and Gaps (model generation)")
    _section7_risks_and_gaps(doc, analysis, model, base_url)

    logger.info("Section 8: Clarification Questions (model generation)")
    _section8_clarification_questions(doc, analysis, model, base_url)

    try:
        doc.save(str(file_path))
    except OSError as exc:
        logger.error("Failed to save document '%s': %s", file_path, exc)
        raise

    resolved = str(file_path.resolve())
    logger.info("Customer summary saved: %s", resolved)
    return resolved
