# Phase 2 — Customer Summary Engine & Product Selector
## Presales AI Platform — Development Journal
**Date:** 8 June 2026
**Author:** Carter Tan
**Version:** v0.2.0
**Status:** ✅ Complete

---

## Overview

Phase 2 extends the Presales AI Platform beyond compliance extraction into
intelligent document generation. The platform can now produce a professional
8-section customer summary Word document automatically from any RFP PDF,
with an interactive product selection step driven by the analyst's expertise.

---

## What Was Built

### 1. `src/summarizer.py` — Customer Summary Generator
**709 lines | Model: granite4.1:30b | Output: .docx**

The summarizer transforms the structured RFP analysis into a professional
Word document ready for internal review before proposal writing begins.

**8-Section Document Structure:**

| Section | Content | Generation Method |
|---------|---------|------------------|
| 1. RFP Overview | Customer, deadline, budget, requirement counts | Extracted data → table |
| 2. Customer Objectives | Strategic goals behind the procurement | granite4.1:30b |
| 3. Identified Use Cases | Specific use cases the solution must address | granite4.1:30b |
| 4. Technical Requirements Summary | Requirements grouped by category | granite4.1:30b |
| 5. Commercial Requirements | SLA, support, timeline, licensing | granite4.1:30b |
| 6. Evaluation Criteria | Scoring breakdown with weights | Extracted data → table |
| 7. Key Risks and Gaps | Ambiguous requirements, compliance gaps | granite4.1:30b |
| 8. Clarification Questions | Questions to ask before submitting | granite4.1:30b |

**Technical implementation:**
- Single Ollama API call generates all AI sections simultaneously
- XML-style section markers for reliable parsing
- Professional Word formatting with dark blue headings (#1F3864)
- Styled tables with header rows
- Auto-saved to `output/summaries/` with timestamped filename
- Full fallback chain: granite4.1:30b → qwq:latest → deepseek-r1:32b

---

### 2. `src/product_selector.py` — Interactive Product Menu
**164 lines | No model required | Output: selected products list**

An interactive terminal menu that presents all 10 Nexus products
for the analyst to select before proposal generation begins.

**Features:**
- Loads product catalog from `config/products.yaml`
- Interactive checkbox menu using `questionary` library
- Displays product name, category (PKI/IAM/Hardware/Mobile), and short code
- Rich-formatted confirmation table showing selected products
- Minimum 1 product validation
- Returns structured list of product dicts for downstream use

**Sample Output:**
```
? Select Nexus products to include in this proposal:
  ◉ Nexus Certificate Manager       (PKI  — NCM)
  ◉ Nexus Smart ID Identity Manager (IAM  — SIIM)
  ◉ Nexus OCSP                      (PKI  — OCSP)
  ◉ Nexus Protocol Gateway          (PKI  — NPG)
  ◯ Nexus m2trust CLM               (PKI  — CLM)
  ...

Selected Products for Proposal
┌───┬─────────────────────────────────┬──────────┬──────────┐
│ # │ Product Name                    │ Category │   Code   │
├───┼─────────────────────────────────┼──────────┼──────────┤
│ 1 │ Nexus Certificate Manager       │ PKI      │   NCM    │
│ 3 │ Nexus Smart ID Identity Manager │ IAM      │   SIIM   │
│ 4 │ Nexus OCSP                      │ PKI      │   OCSP   │
│ 5 │ Nexus Protocol Gateway          │ PKI      │   NPG    │
└───┴─────────────────────────────────┴──────────┴──────────┘
```

---

### 3. `src/main.py` — Updated Pipeline Orchestration

Phase 2 introduced a critical workflow improvement: **analysis results
are displayed before product selection.** This ensures the analyst makes
informed product decisions based on actual customer requirements.

**Updated Pipeline Flow:**
```
1. Extract PDF text          (pdfplumber)
       ↓
2. Analyze RFP               (qwq:latest)
       ↓
3. Display Analysis Results  ← NEW in Phase 2
   • Executive summary
   • Top mandatory requirements
   • Evaluation criteria with weights
   • Win themes and risk areas
       ↓
4. Select Products           ← Informed decision now possible
   (interactive menu)
       ↓
5. Generate Summary Word Doc (granite4.1:30b)
       ↓
6. Display all output paths
```

---

## Issues Encountered and Resolved

| Issue | Root Cause | Resolution |
|-------|-----------|------------|
| Summary generation timed out after 20 min | 8 separate Ollama calls, each reloading model context | Rewrote to single API call with XML section markers |
| `qwen3:32b` fallback returned 404 | Model not installed on this machine | Updated fallback chain to installed models only |
| `qwen3.6:27b` timeout at 180s | Large model + RAM pressure from qwq:latest still loaded | Increased timeout to 300s, switched primary to granite4.1:30b |
| RAM pressure with two 17-19GB models | qwq:latest + qwen3.6:27b = 36GB active simultaneously | Ollama auto-unloads between pipeline stages |
| Product selector called before analysis shown | Wrong pipeline order | Moved analysis display step before product selector |

---

## Model Performance Observations

| Model | Task | Performance | Notes |
|-------|------|-------------|-------|
| `qwq:latest` | RFP analysis and reasoning | ✅ Excellent | Chain-of-thought visible, high quality extraction |
| `granite4.1:30b` | Document section writing | ✅ Fast + Good | IBM enterprise training shows — structured output, professional tone |
| `qwen3.6:27b` | Writing (attempted) | ⚠️ Slow on M5 Pro 64GB | RAM pressure with qwq:latest loaded — works standalone |
| `gemma4:e4b` | Fast fallback | ✅ Very fast | Good for quick tasks |
| `deepseek-r1:32b` | Reasoning backup | ✅ Reliable | Solid fallback when primary unavailable |

---

## File Changes Summary

| File | Status | Lines | Change |
|------|--------|-------|--------|
| `src/summarizer.py` | 🆕 New | 709 | Full Word doc generator |
| `src/product_selector.py` | 🆕 New | 164 | Interactive product menu |
| `src/main.py` | ✏️ Updated | — | Phase 2 pipeline, analysis display before selection |
| `config/models.yaml` | ✏️ Updated | — | Writing model updated to granite4.1:30b |
| `.env` | ✏️ Updated | — | OLLAMA_WRITING_MODEL=granite4.1:30b |
| `JOURNAL.md` | ✏️ Updated | — | Phase 2 session log appended |

---

## Phase 2 Outputs

Running `python src/main.py --rfp your-rfp.pdf` now produces:

```
output/
├── compliance/
│   └── CustomerName_Compliance_20260608.xlsx    ← Phase 1
└── summaries/
    └── CustomerName_Summary_20260608.docx       ← Phase 2 NEW
```

---

## Key Decisions Made in Phase 2

**1. Single API call over multiple calls**
Generating all 8 Word sections in one Ollama call is dramatically faster
than 8 separate calls. The XML parsing approach proved reliable.

**2. granite4.1:30b over qwen3.6:27b for writing**
IBM Granite's enterprise training data makes it naturally suited for
professional document generation. It produces more structured, formal
output with less prompt engineering needed.

**3. Analysis-first workflow**
Showing the RFP analysis results before product selection transforms
the tool from an automation into a decision-support system. The analyst
sees what the customer needs, then selects products intelligently.

**4. Informed product selection**
The product selector now serves a strategic purpose — not just picking
products but matching them to the extracted customer requirements.

---

## Next — Phase 3

**Target:** Full proposal generator with RAG knowledge base

| File | What Gets Built |
|------|----------------|
| `src/rag/indexer.py` | Ingest past proposals and product docs into ChromaDB |
| `src/rag/retriever.py` | Semantic search over knowledge base |
| `src/proposal.py` | Full 17-section Word proposal generator |
| `knowledge/products/*.md` | Populated with Nexus product descriptions |

**How to populate knowledge base:**
```bash
# Drop past proposals into knowledge/proposals/
# Then run:
python src/rag/indexer.py
```

---

## GitHub Release

**Tag:** v0.2.0
**Repo:** [github.com/cartertan/presales-ai-platform](https://github.com/cartertan/presales-ai-platform)

---

*Carter Tan · AI Architect Journey · Session 2 · 8 June 2026*
*Project 2 of 8 · Phase 2 of 5*
