# CLAUDE.md — Presales AI Platform

## Project Overview
AI-powered presales platform transforming RFP PDFs into:
- Compliance matrix Excel
- Customer summary Word doc
- Draft Word proposal
- PowerPoint presentation

Zero cloud cost. Runs entirely on local Ollama models.

## Key Commands
- Full pipeline: python src/main.py --rfp data/rfp/your-rfp.pdf
- Phase 1 only: python src/main.py --rfp data/rfp/your-rfp.pdf --phase 1
- Index knowledge: python src/rag/indexer.py
- Run tests: pytest tests/ -v

## Model Assignments (June 2026)
- qwq:latest           — RFP analysis and reasoning (primary)
- granite4.1:30b       — Compliance content and enterprise writing
- qwen3.6:27b          — Proposal writing, summaries, PPT content
- devstral:latest      — Agentic coding tasks
- gemma4:e4b           — Fast tasks and vision (RFP diagrams)
- deepseek-r1:32b      — Reasoning backup
- nomic-embed-text     — RAG embeddings

## Products (10 Nexus Products)
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

## Industries
eGovernment, Citizen ID, Telco, Banking and Finance,
Energy, Oil and Gas, Insurance, Trust Centers, Manufacturing

## Coding Standards
- Type hints on all functions
- Docstrings on all functions
- Use logging not print()
- Load all config from .env
- No bare except clauses
- Run pytest before every commit
- Never commit .env or customer PDFs
