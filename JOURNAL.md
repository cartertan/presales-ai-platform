# Development Journal

## Session 1 — 26 May 2026
**Author:** Carter Tan
**Project:** Presales AI Platform
**Duration:** Full day session
**Status:** Phase 1 Complete ✅

---

### What Was Accomplished Today

#### 1. Project Architecture Designed
- Designed full 5-phase system architecture
- Defined pipeline: RFP PDF → Analysis → Compliance Excel → Summary → Proposal → PPT
- Documented all 17 Word proposal sections
- Documented PPT slide structure for customer presentations
- Published architecture to GitHub as ARCHITECTURE.md and docs/

#### 2. Local AI Model Stack Assessed and Updated
Assessed 7 locally installed Ollama models and assigned optimal model per task:

| Task | Model Assigned | Reason |
|------|---------------|--------|
| RFP analysis and reasoning | qwq:latest | Newest reasoning model, chain-of-thought |
| Compliance and enterprise content | granite4.1:30b | IBM enterprise model, regulatory expertise |
| Proposal and summary writing | qwen3.6:27b | Newest Qwen generation, best writing quality |
| PPT content generation | qwen3.6:27b | Concise structured output |
| Fast pre-processing and vision | gemma4:e4b | Vision capable, fast responses |
| Agentic coding | devstral:latest | Purpose-built for multi-file code operations |
| Reasoning backup | deepseek-r1:32b | Fallback model |
| RAG embeddings | nomic-embed-text | Industry standard embeddings |

#### 3. Project Foundation Built
Created complete project structure under ~/AI-Projects/presales-ai-platform/:

**Folder structure created:**
- src/ — Python source files
- src/rag/ — RAG indexer and retriever
- config/ — YAML configuration files
- knowledge/products/ — 10 Nexus product knowledge files
- knowledge/industries/ — 9 industry vertical files
- knowledge/proposals/ — Past proposals repository (gitignored)
- knowledge/templates/ — Word and PPT base templates
- output/compliance/ — Generated Excel matrices
- output/summaries/ — Generated Word summaries
- output/proposals/ — Generated Word proposals
- output/presentations/ — Generated PowerPoint files
- tests/ — Automated test suite
- docs/ — Architecture and user guide

**Configuration files created:**
- config/products.yaml — 10 Nexus products catalog with descriptions
- config/industries.yaml — 9 industry verticals with key requirements
- config/models.yaml — Model assignments per task
- .env.example — Environment configuration template with 7 models
- .gitignore — Excludes .env, proposals/, PDFs, chroma_db/, output/
- requirements.txt — All Python dependencies
- CLAUDE.md — Project-specific instructions for Claude Code

**Dependencies installed:**
- pdfplumber — PDF text extraction
- python-dotenv — Environment variable management
- requests — Ollama API communication
- pyyaml — YAML config file parsing
- python-docx — Word document generation
- python-pptx — PowerPoint generation
- openpyxl — Excel file creation
- rich — Beautiful terminal output
- questionary — Interactive product selection menu
- pytest — Automated testing

#### 4. Phase 1 Source Files Built by Claude Code
Claude Code (AI coding assistant) built all 4 Python source files:

**src/extractor.py**
- Function: extract_pdf_text(file_path: str) -> dict
- Reads any RFP PDF using pdfplumber
- Extracts text page by page
- Returns structured dict with file_name, page_count, word_count, full_text, pages
- Handles scanned PDFs, missing files, invalid formats
- Full type hints, docstrings, and logging

**src/analyzer.py**
- Function: check_ollama(base_url: str) -> bool
- Function: analyze_rfp(text: str, config: dict) -> dict
- Calls qwq:latest via Ollama API at localhost:11434
- Extracts: requirements list, mandatory/optional classification,
  scoring weights, customer objectives, evaluation criteria,
  submission deadline, budget, industry vertical, win themes, risks
- Falls back to deepseek-r1:32b if primary model unavailable
- Full error handling and structured JSON output

**src/compliance.py**
- Function: generate_excel(analysis: dict, output_dir: str) -> str
- Creates color-coded Excel compliance matrix using openpyxl
- Sheet 1: Full compliance matrix with 10 columns
  * Red rows = MANDATORY requirements
  * Yellow rows = OPTIONAL requirements
  * Orange cells = Risk flagged items
  * Grey cells = TBC status
  * Frozen header row, auto-fit columns
- Sheet 2: RFP summary with evaluation criteria and win themes
- Returns path to saved Excel file

**src/main.py**
- CLI entry point using argparse
- Beautiful terminal output using rich library
- Arguments: --rfp, --phase, --output
- Checks Ollama is running before starting
- Orchestrates full Phase 1 pipeline
- Saves analysis JSON for reuse in later phases
- Shows summary table of all outputs at completion

#### 5. Tested With Real RFP
- Tested with: RFQ2600170 Public Key Infrastructure.pdf
- Pipeline completed successfully
- Extracted requirements correctly identified as mandatory/optional
- Compliance Excel generated with color coding
- Analysis model: qwq:latest with deepseek-r1:32b backup

---

### Key Decisions Made Today

1. **New separate repo** — presales-ai-platform is separate from rfp-analyzer
2. **qwq:latest replaces deepseek-r1:32b as primary** — newer, better reasoning
3. **granite4.1:30b added** — IBM enterprise model perfect for compliance content
4. **qwen3.6:27b upgraded** — replaces qwen3:32b for all writing tasks
5. **devstral:latest added** — agentic coding for Claude Code sessions
6. **gemma4:e4b added** — fills vision gap for reading RFP diagrams

---

### Issues Encountered and Resolved

| Issue | Resolution |
|-------|-----------|
| Heredoc escaping errors in terminal | Switched to Python file write approach |
| deepseek-r1:70b RAM crash | Replaced with 32B version |
| brew upgrade ollama failed | Ollama was installed via native app, not brew |
| git remote already exists error | Used git remote remove origin before re-adding |

---

### Next Session — Phase 2 Plan

**Phase 2 targets:**
- src/summarizer.py — Customer summary Word document (qwen3.6:27b)
- src/product_selector.py — Interactive product selection menu (questionary)
- Test with real RFP end-to-end producing both Excel and Word summary
- GitHub: v0.2.0 tag

**Knowledge base population needed:**
- Add product descriptions to knowledge/products/*.md files
- Source: Nexus Copilot content
- Add 1-2 past proposals to knowledge/proposals/
- Run: python src/rag/indexer.py to build ChromaDB

---

### GitHub Repositories Updated Today

| Repo | Version | What Was Added |
|------|---------|----------------|
| cartertan/rfp-analyzer | v0.1.0 | Original RFP analyzer MVP — Phase 1 complete |
| cartertan/presales-ai-platform | v0.1.0 | Full presales platform Phase 1 foundation |

---
*Carter Tan · AI Architect Journey · Session 1 of 6 months · 26 May 2026*

## Phase 2 Complete — 8 June 2026
See full write-up: [docs/PHASE2_SUMMARY.md](docs/PHASE2_SUMMARY.md)

## Phase 2 Complete — 8 June 2026
See full write-up: [docs/PHASE2_SUMMARY.md](docs/PHASE2_SUMMARY.md)


---

## Phase 3 Complete — 9 June 2026
**Version:** v0.3.0

RAG knowledge base fully built and indexed.

- src/rag/indexer.py: ChromaDB ingestion pipeline
- src/rag/retriever.py: Semantic search engine
- 11 product knowledge files populated
- 10 industry knowledge files populated (inc. V2G/Hubject)
- 287 chunks indexed in ChromaDB
- Safaricom proposal indexed as first reference

See full write-up: docs/PHASE3_SUMMARY.md
See lessons learned: docs/LESSONS_LEARNED_SESSION3.md

---

## Phase 4 Complete — 10 June 2026
**Version:** v0.4.0
**Status:** Complete

17-section Word proposal generator built (src/proposal.py, 1369 lines).

**Models used:**
- qwq:latest — RFP analysis and reasoning
- granite4.1:30b — Compliance writing (sections requiring regulatory/enterprise tone)
- qwen3.6:27b — Company profile and customer references
- deepseek-r1:32b — Assumptions section

**Pipeline:** ~8 minutes for full 5-step pipeline

**Output:** RFQ2600170_Public_Key_Inf_Proposal_Draft_20260610.docx

**Key decisions:**
- Multi-model strategy: each section type assigned to the model best suited for it
- XML markers used for parsing model output cleanly across all sections
- Sections 12–14 combined into a single call to reduce round-trips and preserve flow

**BLANK placeholders (intentional — require human input):**
- Section 5: Solution Architecture
- Section 8: Technical Sizing
- Section 15: Project Timeline
- Section 16: Commercials

**Next phase:** Phase 5 — PowerPoint generator

---

## Phase 5 — PowerPoint Deck Generator
**Date:** 2026-06-15
**Version:** v0.5.0
**Status:** ✅ Complete

### What Was Built
- `src/pptgen.py` — 15-slide branded .pptx generator
- Slides auto-populated from RFP analysis, product selection, and RAG knowledge
- Nexus brand colors applied: navy #1F3864 headers, teal #0097A7 accents
- Speaker notes generated per slide via gemma4:e4b

### Models Used
| Task | Model |
|------|-------|
| Slide bullet summarization | granite4.1:30b |
| Executive narrative | qwen3.6:27b |
| Speaker notes | gemma4:e4b |

### Pipeline — Final State
| Step | Output |
|------|--------|
| 1 | PDF extracted |
| 2 | RFP analysis JSON |
| 2b | Analysis JSON saved |
| 3 | Compliance Excel matrix |
| 4 | Customer summary Word doc |
| 5 | Proposal draft Word doc |
| 6 | Presentation deck .pptx |

### Key Decisions
- One Ollama call per slide section — consistent with Phase 4 pattern
- XML markers for reliable bullet parsing
- Architecture and pricing slides left as human-input placeholders
- Deck reads directly from analysis JSON — no reprocessing needed

### Metrics
- Pipeline time: ~10 minutes end-to-end
- External API cost: $0
- Lines of code: ~600 (pptgen.py)

### Lessons Learned
- python-pptx layout indexes matter — wrong index silently breaks formatting
- Brand colors applied at shape level, not theme level, for reliability
- Speaker notes field is underused but high value for customer meetings

### Next
- Project 3 planning begins
- LinkedIn full pipeline announcement posted
- Claude memory updated