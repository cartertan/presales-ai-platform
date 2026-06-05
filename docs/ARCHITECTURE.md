# Presales AI Platform
### Complete System Architecture & Implementation Plan
> RFP Analyzer · Proposal Generator · PPT Engine · Knowledge Repository

**Author:** Carter Tan · AI Architect Journey · May 2026 · v1.0

---

## Table of Contents
1. [Executive Summary](#1-executive-summary)
2. [System Architecture](#2-system-architecture)
3. [Complete Folder Structure](#3-complete-folder-structure)
4. [Compliance Matrix Excel Design](#4-compliance-matrix-excel-design)
5. [Word Proposal Document Structure](#5-word-proposal-document-structure)
6. [PowerPoint Presentation Structure](#6-powerpoint-presentation-structure)
7. [Knowledge Repository Strategy](#7-knowledge-repository-strategy)
8. [Complete CLI Workflow](#8-complete-cli-workflow)
9. [Implementation Phases](#9-implementation-phases)
10. [Python Dependencies](#10-python-dependencies)
11. [Immediate Next Steps](#11-immediate-next-steps)

---

## 1. Executive Summary

The **Presales AI Platform** is a locally-hosted, zero-cloud-cost AI system that transforms any RFP PDF into a compliance matrix, customer summary, draft Word proposal, and PowerPoint presentation — using only local Ollama models. All customer data stays on your MacBook. The system uses your past proposals as a knowledge base to improve output quality over time.

### Core Capabilities
- Analyze RFP using `deepseek-r1:32b` chain-of-thought reasoning
- Extract compliance requirements with mandatory/optional scoring into Excel
- Generate customer summary Word document
- Interactive product selection (10 Nexus products)
- Generate full draft Word proposal from templates + knowledge base
- Generate customer PowerPoint presentation with branding
- Local knowledge repository with RAG semantic search over past proposals
- Google Drive MCP integration ready for future cloud sync

---

## 2. System Architecture

### Pipeline Overview

```
RFP PDF Input
     │
     ▼
┌─────────────────────────────────────────────────┐
│  STAGE 1: EXTRACTION                            │
│  extractor.py → pdfplumber → raw text + pages  │
└─────────────────────────────────────────────────┘
     │
     ▼
┌─────────────────────────────────────────────────┐
│  STAGE 2: ANALYSIS  (deepseek-r1:32b)           │
│  analyzer.py → requirements, scoring, risks     │
└─────────────────────────────────────────────────┘
     │
     ├──────────────────────────┐
     ▼                          ▼
┌──────────────────┐   ┌─────────────────────┐
│ compliance.py    │   │ summarizer.py       │
│ Excel matrix     │   │ Word summary doc    │
│ (mandatory/opt.) │   │ (qwen3:32b)         │
└──────────────────┘   └─────────────────────┘
     │
     ▼  (user selects products)
┌─────────────────────────────────────────────────┐
│  STAGE 3: KNOWLEDGE RETRIEVAL                   │
│  rag/retriever.py → ChromaDB semantic search   │
│  Finds: past proposals + product info           │
└─────────────────────────────────────────────────┘
     │
     ├──────────────────────────┐
     ▼                          ▼
┌──────────────────┐   ┌─────────────────────┐
│ proposal.py      │   │ ppt_generator.py    │
│ Word .docx       │   │ PowerPoint .pptx    │
│ (qwen3:32b)      │   │ (qwen3:32b)         │
└──────────────────┘   └─────────────────────┘
```

### Model Assignment

| Task | Model | Why |
|------|-------|-----|
| RFP reasoning & requirement extraction | `deepseek-r1:32b` | Chain-of-thought — shows reasoning steps, best for complex logical analysis |
| Mandatory vs optional classification | `deepseek-r1:32b` | Structured logical scoring, reduces hallucination |
| Customer summary writing | `qwen3:32b` | Best long-form professional writing quality |
| Proposal draft generation | `qwen3:32b` | 128K context — handles full proposal in one pass |
| PPT slide content | `qwen3:32b` | Concise structured output, understands slide format |
| Fast pre-processing | `mistral:7b` | Section detection, text cleanup — 2 second response |
| RAG embeddings | `nomic-embed-text` | Industry standard, tiny footprint, always running |

---

## 3. Complete Folder Structure

```
presales-ai-platform/
├── CLAUDE.md                    ← Project instructions for Claude Code
├── README.md                    ← GitHub documentation
├── .gitignore                   ← Excludes: .env, proposals/, *.pdf
├── .env.example                 ← Config template
├── requirements.txt             ← All Python dependencies
│
├── config/
│   ├── products.yaml            ← Your 10 Nexus products catalog
│   ├── industries.yaml          ← 9 industry verticals
│   └── models.yaml              ← Model assignments per task
│
├── src/
│   ├── main.py                  ← CLI orchestrator (argparse)
│   ├── extractor.py             ← PDF text extraction (pdfplumber)
│   ├── analyzer.py              ← RFP analysis (deepseek-r1:32b)
│   ├── compliance.py            ← Compliance matrix → Excel (openpyxl)
│   ├── summarizer.py            ← Customer summary → Word (qwen3:32b)
│   ├── product_selector.py      ← Interactive product selection menu
│   ├── proposal.py              ← Word proposal generator (qwen3:32b)
│   ├── ppt_generator.py         ← PPT generator (qwen3:32b + pptx)
│   └── rag/
│       ├── indexer.py           ← Ingest docs to ChromaDB
│       └── retriever.py         ← Semantic search query
│
├── knowledge/
│   ├── products/                ← Product knowledge files (markdown)
│   │   ├── nexus-certificate-manager.md
│   │   ├── nexus-smart-id-digital-access.md
│   │   ├── nexus-smart-id-identity-manager.md
│   │   ├── nexus-ocsp.md
│   │   ├── nexus-protocol-gateway.md
│   │   ├── nexus-m2trust-clm.md
│   │   ├── cosmo-smartcard.md
│   │   ├── idplug-middleware.md
│   │   ├── nexus-mobile-client.md
│   │   └── smart-desktop-application.md
│   │
│   ├── industries/              ← Industry-specific content
│   │   ├── egovernment.md
│   │   ├── citizen-id.md
│   │   ├── telco.md
│   │   ├── banking.md
│   │   ├── energy.md
│   │   ├── oil-gas.md
│   │   ├── insurance.md
│   │   ├── trust-centers.md
│   │   └── manufacturing.md
│   │
│   ├── proposals/               ← Your past proposals (GITIGNORED)
│   │   └── [your past proposals go here — Word/PDF]
│   │
│   └── templates/               ← Base templates
│       ├── proposal-template.docx
│       └── presentation-template.pptx
│
├── chroma_db/                   ← Vector database (GITIGNORED)
│
├── output/                      ← All generated files (GITIGNORED)
│   ├── compliance/              ← Excel compliance matrices
│   ├── summaries/               ← Word summary documents
│   ├── proposals/               ← Generated Word proposals
│   └── presentations/           ← Generated PowerPoint files
│
├── tests/
│   ├── test_extractor.py
│   ├── test_analyzer.py
│   ├── test_compliance.py
│   └── test_rag.py
│
└── docs/
    ├── architecture.md
    └── user-guide.md
```

---

## 4. Compliance Matrix Excel Design

The compliance Excel file is the first output of the pipeline. It is designed to be submittable to the customer and editable by you.

### Excel Column Structure

| Column | Field Name | Content | Source |
|--------|-----------|---------|--------|
| A | Req ID | RFP-001, RFP-002... | Auto-generated |
| B | Section | Section from RFP | deepseek-r1 extracted |
| C | Requirement | Full requirement text | deepseek-r1 extracted |
| D | Type | MANDATORY / OPTIONAL | deepseek-r1 classified |
| E | Customer Scoring Weight | %, points, or High/Med/Low | deepseek-r1 extracted |
| F | Compliance Status | Fully / Partially / Not / TBC | You fill in |
| G | Nexus Solution | Which product addresses this | Auto-suggested |
| H | Your Response | Your compliance statement | You fill in |
| I | Supporting Docs | Reference doc or section | You fill in |
| J | Remarks / Risks | Flags, gaps, notes | deepseek-r1 flagged |

### Color Coding

| Color | Meaning | Applied To |
|-------|---------|-----------|
| 🔴 Red fill | MANDATORY requirement | Entire row |
| 🟡 Yellow fill | OPTIONAL requirement | Entire row |
| 🟠 Orange fill | Risk or gap flagged | Column J |
| 🟢 Green fill | Fully compliant | Column F |
| ⚪ Grey fill | TBC — needs your input | Column F |

---

## 5. Word Proposal Document Structure

Sections marked **[AUTO]** are filled by the AI.
Sections marked **[YOU]** require your input.
Sections marked **[BLANK+TABLE]** are left blank with a placeholder table.

| Section | Title | Source | Notes |
|---------|-------|--------|-------|
| 1 | Executive Summary | [AUTO] qwen3:32b | Generated from RFP analysis |
| 2 | Understanding of Requirements | [AUTO] qwen3:32b | From customer summary |
| 3 | Proposed Solution Overview | [AUTO] selected products | From product knowledge base |
| 4 | Solution Architecture | [BLANK+TABLE] [YOU] | Customer-specific — you fill in |
| 5 | Product Descriptions | [AUTO] knowledge base | From products/*.md files |
| 6 | Compliance Statement | [AUTO] compliance matrix | From Excel output |
| 7 | Technical Sizing | [BLANK+TABLE] [YOU] | VM, CPU, storage — you fill in |
| 8 | Scope of Work | [AUTO] generic + [YOU] | Generic SOW + your additions |
| 9 | Assumptions & Dependencies | [AUTO] deepseek-r1 | From risk analysis |
| 10 | Implementation Approach | [AUTO] generic | Standard Nexus methodology |
| 11 | Project Management | [AUTO] generic | Standard PM approach |
| 12 | Support Model | [AUTO] generic | Standard support tiers |
| 13 | Training | [AUTO] generic | Standard training offering |
| 14 | Project Timeline | [BLANK+TABLE] [YOU] | Gantt placeholder |
| 15 | Commercials | [BLANK+TABLE] [YOU] | Pricing — you fill in |
| 16 | Company Profile | [AUTO] knowledge base | Nexus company overview |
| 17 | References | [AUTO] past proposals | From proposals/ folder |

---

## 6. PowerPoint Presentation Structure

Generated in 1-2 hours. Uses your existing `brand-theme` skill for styling. Designed for a 30-45 minute customer presentation.

| Slide | Title | Content Source |
|-------|-------|---------------|
| 1 | Title Slide | Customer name + solution name + date |
| 2 | Agenda | Auto-generated from slide deck |
| 3 | Understanding Your Requirements | From RFP summary |
| 4 | Your Challenges | Extracted from RFP pain points |
| 5 | Proposed Solution Overview | Selected products diagram |
| 6-N | Product Deep Dives | One slide per selected product |
| N+1 | Solution Architecture | Generic reference architecture |
| N+2 | Use Cases We Address | Industry-specific use cases |
| N+3 | Why Nexus | Differentiators from knowledge base |
| N+4 | Customer References | From past proposals |
| N+5 | Implementation Approach | Timeline overview |
| N+6 | Next Steps | Blank — you fill in |
| Last | Thank You / Contact | Your contact details |

---

## 7. Knowledge Repository Strategy

### Phase 1 — Mac Local (Now)
- All files stored under `~/AI-Projects/presales-ai-platform/knowledge/`
- ChromaDB vector database stored locally at `./chroma_db/`
- Past proposals in `knowledge/proposals/` (gitignored — confidential)
- Product knowledge in `knowledge/products/` as markdown files
- Indexed automatically on first run

### Phase 2 — Google Drive MCP (Future)
- Google Drive MCP already connected to your Claude setup
- Sync `knowledge/` folder to Google Drive using MCP
- Claude Code can query Google Drive directly for document retrieval
- No code changes needed — just update the retriever to check Drive MCP
- Trigger: say `"sync knowledge base to Google Drive"`

### Technical Knowledge Import Strategy

| Source | Method | Where It Goes |
|--------|--------|---------------|
| Nexus Copilot daily chats | Export key content → paste into product `.md` files | `knowledge/products/` |
| Past proposals (Word/PDF) | Drop into `knowledge/proposals/` → run indexer | ChromaDB vector DB |
| Product datasheets | Drop into `knowledge/products/` as PDF → auto-indexed | ChromaDB vector DB |
| Architecture diagrams | Save as PNG → reference in product `.md` files | `knowledge/products/images/` |
| Claude Memory | Summaries stored after each project completion | Claude memory system |
| CLAUDE.md | Project-level instructions and key product facts | Project root |

---

## 8. Complete CLI Workflow

```bash
python src/main.py --rfp data/rfp/customer-rfp.pdf
```

```
═══════════════════════════════════════════════
  PRESALES AI PLATFORM v1.0
═══════════════════════════════════════════════

📄 Loading RFP: customer-rfp.pdf (47 pages, 14,200 words)

🧠 Analyzing with deepseek-r1:32b...
   <think> Identifying mandatory requirements... </think>
   ✅ Found 34 requirements (22 mandatory, 12 optional)
   ✅ Detected scoring: Technical 40%, Experience 30%, Price 20%, PM 10%

📊 Generating compliance matrix...
   ✅ Saved: output/compliance/Customer_Compliance_20260526.xlsx

📝 Generating customer summary...
   ✅ Saved: output/summaries/Customer_Summary_20260526.docx

═══════════════════════════════════════════════
  SELECT PRODUCTS TO PROPOSE
═══════════════════════════════════════════════
  1. Nexus Certificate Manager
  2. Nexus Smart ID Digital Access
  3. Nexus Smart ID Identity Manager
  4. Nexus OCSP
  5. Nexus Protocol Gateway
  6. Nexus m2trust CLM
  7. Cosmo Smartcard
  8. IDPlug Middleware
  9. Nexus Mobile Client
 10. Smart Desktop Application

Enter product numbers (e.g. 1,2,4,7): 1,2,4

🔍 Searching knowledge base for relevant content...
   ✅ Found 3 similar past proposals
   ✅ Loaded product info: Certificate Manager, Smart ID, OCSP

📄 Generating proposal draft (qwen3:32b)...
   ✅ Saved: output/proposals/Customer_Proposal_Draft_20260526.docx

🎯 Generating presentation (qwen3:32b)...
   ✅ Saved: output/presentations/Customer_Presentation_20260526.pptx

═══════════════════════════════════════════════
  COMPLETE — 4 outputs generated in 4m 32s
═══════════════════════════════════════════════
  ✅ Compliance Excel:   output/compliance/
  ✅ Summary Word Doc:   output/summaries/
  ✅ Proposal Draft:     output/proposals/
  ✅ Presentation:       output/presentations/
```

---

## 9. Implementation Phases

| Phase | What Gets Built | Key Files | Time | Models Used |
|-------|----------------|-----------|------|-------------|
| **1** | Project setup + PDF extraction + deepseek analysis + compliance Excel | `extractor.py`, `analyzer.py`, `compliance.py` | 3-4 hrs | `deepseek-r1:32b`, `mistral:7b` |
| **2** | Customer summary Word doc + product selector menu | `summarizer.py`, `product_selector.py` | 2-3 hrs | `qwen3:32b` |
| **3** | Knowledge repository + RAG indexer + retriever | `rag/indexer.py`, `rag/retriever.py`, `knowledge/` files | 4-5 hrs | `nomic-embed-text`, `qwen3:32b` |
| **4** | Full Word proposal generator with all 17 sections | `proposal.py`, `templates/proposal-template.docx` | 4-5 hrs | `qwen3:32b` |
| **5** | PowerPoint generator with brand theme | `ppt_generator.py`, `templates/presentation-template.pptx` | 3-4 hrs | `qwen3:32b` |
| **6** | CLI orchestrator + end-to-end testing + GitHub | `main.py`, `tests/`, `README.md` | 2-3 hrs | All models |

### Phase 1 Deliverables (Start Today)
- Complete project folder structure created
- All config files: `products.yaml`, `industries.yaml`, `models.yaml`
- `extractor.py` — PDF text extraction (ported from rfp-analyzer)
- `analyzer.py` — `deepseek-r1:32b` RFP analysis with mandatory/optional detection
- `compliance.py` — openpyxl Excel generation with color coding
- GitHub repo: `presales-ai-platform` v0.1.0 tagged

---

## 10. Python Dependencies

```txt
# Core
pdfplumber==0.11.4           # PDF text extraction
python-dotenv==1.0.1         # Environment variables
requests==2.32.3             # Ollama API calls
pyyaml==6.0.2                # Config files

# Document generation
python-docx==1.1.2           # Word document creation
python-pptx==1.0.2           # PowerPoint generation
openpyxl==3.1.5              # Excel file creation

# Knowledge base / RAG
chromadb==0.6.3              # Local vector database
sentence-transformers==3.3.1 # Embeddings backup

# CLI and utilities
rich==13.9.4                 # Beautiful terminal output
questionary==2.0.1           # Interactive product selection
pytest==8.3.2                # Testing
```

### Install Command

```bash
pip install pdfplumber python-dotenv requests pyyaml \
  python-docx python-pptx openpyxl chromadb \
  sentence-transformers rich questionary pytest
```

---

## 11. Immediate Next Steps

| Priority | Action | Notes |
|----------|--------|-------|
| 1 | Approve this architecture | Tell Claude: `approved — start Phase 1` |
| 2 | Create new GitHub repo | Name: `presales-ai-platform` |
| 3 | Claude Code builds Phase 1 | Follow the Phase 1 build guide |
| 4 | Populate product knowledge files | Add Nexus Copilot content to `knowledge/products/` |
| 5 | Add past proposals to repo | Drop Word/PDF into `knowledge/proposals/` |
| 6 | Test with real RFP | `python src/main.py --rfp your-rfp.pdf` |

---

## About This Project

**Author:** Carter Tan
**Role:** Solutions Architect & AI Security Specialist
**Journey:** 6-Month AI Architect Program (June–November 2026)
**Stack:** Python · Ollama · deepseek-r1:32b · qwen3:32b · ChromaDB · Claude Code

> Built entirely on local Ollama models — zero cloud cost, complete data privacy.

---

*Part of the [AI Architect Journey](https://github.com/cartertan) — 8 projects in 6 months.*
