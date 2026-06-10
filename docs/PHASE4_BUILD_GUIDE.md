# Phase 4 — Full Proposal Generator
## Presales AI Platform — Step-by-Step Build Guide
**Date:** 10 June 2026
**Version Target:** v0.4.0
**Prerequisite:** Phase 3 RAG complete — 287 chunks indexed

---

## What Phase 4 Builds

The proposal generator is the centrepiece of the entire platform.
It takes everything built in Phases 1-3 and produces a complete,
professional Word document proposal — ready to edit and submit.

### Pipeline Position
```
Phase 1: RFP PDF → Analysis → Compliance Excel
Phase 2: Customer Summary Word Doc + Product Selection
Phase 3: RAG Knowledge Base (287 chunks)
          ↓
Phase 4: proposal.py
          ↓ Retrieves from RAG
          ↓ Uses analysis from Phase 1
          ↓ Uses selected products from Phase 2
          ↓ Generates 17-section Word proposal
          ↓
    output/proposals/CustomerName_Proposal_Draft.docx
```

---

## Phase 4 Deliverables

| Deliverable | Description | Model |
|-------------|-------------|-------|
| src/proposal.py | 17-section Word proposal generator | qwen3.6:27b + granite4.1:30b |
| output/proposals/*.docx | Generated proposal drafts | — |
| Updated main.py | Phase 4 integrated into pipeline | — |
| GitHub v0.4.0 | Tagged release | — |

---

## The 17-Section Proposal Structure

| # | Section | Method | Who Fills |
|---|---------|--------|-----------|
| 1 | Cover Page | AUTO | Template |
| 2 | Executive Summary | AUTO — qwen3.6:27b | AI |
| 3 | Understanding of Requirements | AUTO — from RFP analysis | AI |
| 4 | Proposed Solution Overview | AUTO — from selected products | AI + RAG |
| 5 | Solution Architecture | BLANK + TABLE | You |
| 6 | Product Descriptions | AUTO — from RAG knowledge base | RAG |
| 7 | Compliance Statement | AUTO — from compliance matrix | AI |
| 8 | Technical Sizing | BLANK + TABLE | You |
| 9 | Scope of Work | AUTO generic + placeholder | AI |
| 10 | Assumptions and Dependencies | AUTO — deepseek-r1:32b | AI |
| 11 | Implementation Approach | AUTO generic | AI |
| 12 | Project Management | AUTO generic | AI |
| 13 | Support Model | AUTO generic | AI |
| 14 | Training | AUTO generic | AI |
| 15 | Project Timeline | BLANK + TABLE | You |
| 16 | Commercials | BLANK + TABLE | You |
| 17 | Company Profile | AUTO — from RAG | RAG |

---

## STEP 1 — Create Git Branch

```bash
cd ~/AI-Projects/presales-ai-platform
git checkout -b phase-4-proposal
git branch
```

---

## STEP 2 — Create Phase 4 Plan File

```bash
python3 << 'PYEOF2'
import os
os.makedirs("docs/plans", exist_ok=True)
plan = open("docs/plans/2026-06-10-phase4.md", "w")
plan.write("""# Phase 4 Plan — Proposal Generator
Date: 10 June 2026

## Files To Build
- src/proposal.py: 17-section Word proposal generator

## Files To Update
- src/main.py: Add Phase 4 to pipeline

## Model Assignments
- qwen3.6:27b: Executive summary, solution overview, SOW
- granite4.1:30b: Compliance statement, assumptions, technical sections
- RAG retriever: Product descriptions, company profile, references

## Tasks
- [ ] Build generate_proposal() function
- [ ] Build all 17 section generators
- [ ] Integrate RAG retrieval per section
- [ ] Professional Word formatting
- [ ] Update main.py pipeline
- [ ] End-to-end test with real RFP
""")
plan.close()
print("Phase 4 plan created")
PYEOF2
```

---

## STEP 3 — Open Claude Code

```bash
cd ~/AI-Projects/presales-ai-platform
claude
```

Paste this prompt exactly:

```
Read CLAUDE.md carefully. Then read these files in order:
1. src/analyzer.py — understand the analysis dict structure
2. src/product_selector.py — understand selected products structure
3. src/rag/retriever.py — understand how to call search_products(),
   search_industries(), search_proposals(), format_context()
4. src/summarizer.py — understand the Word document patterns used

Now build src/proposal.py — the 17-section proposal generator.

IMPORTANT RULES:
- Load writing model from env: OLLAMA_WRITING_MODEL (qwen3.6:27b)
- Load compliance model from env: OLLAMA_COMPLIANCE_MODEL (granite4.1:30b)
- Use single Ollama API call per major section — not one per paragraph
- Use RAG retriever for sections that need knowledge base content
- All Word formatting must use python-docx
- Professional styling: dark blue headings #1F3864, styled tables
- Every section that needs AI content uses XML markers for reliable parsing
- BLANK sections get a placeholder paragraph + formatted empty table
- Full logging throughout
- Full type hints and docstrings

BUILD THIS FUNCTION:

def generate_proposal(
    analysis: dict,
    selected_products: list,
    output_dir: str,
    config: dict
) -> str

The analysis dict comes from analyzer.py and contains:
- executive_summary, requirements, evaluation_criteria
- customer_objectives, win_themes, risk_areas
- submission_deadline, budget, industry_vertical

The selected_products list contains product dicts with:
- name, short, category, description

The config dict contains:
- ollama_base_url, writing_model, compliance_model

The function should:
1. Create a Word document with professional styling
2. Generate all 17 sections as described below
3. Save to output_dir/proposals/{customer_name}_Proposal_Draft_{YYYYMMDD}.docx
4. Return the path to the saved file

SECTION DETAILS:

SECTION 1 — Cover Page
- Large title: "Technical Proposal"
- Subtitle: solution name based on selected products
- Field: "Prepared for: [CUSTOMER NAME]" — extract from analysis
- Field: "Prepared by: Nexus"
- Field: "Date: {today}"
- Field: "Version: 1.0 — DRAFT"
- Field: "Classification: Confidential"
- Page break after

SECTION 2 — Executive Summary
Model: qwen3.6:27b
RAG: search_products(product names, n=3) + search_industries(industry, n=2)
Prompt context: analysis executive_summary + win_themes + selected products
Generate: 3-4 paragraphs positioning Nexus solution for this customer
XML marker: <exec_summary>...</exec_summary>

SECTION 3 — Understanding of Customer Requirements
Model: qwen3.6:27b
Source: analysis customer_objectives + requirements list
Generate: 2-3 paragraphs showing deep understanding of what customer needs
Then: Table of top 10 mandatory requirements with Req ID, Requirement, Priority
XML marker: <understanding>...</understanding>

SECTION 4 — Proposed Solution Overview
Model: qwen3.6:27b
RAG: search_products(selected product names joined, n=5)
Generate: Overview paragraph then one paragraph per selected product
explaining how it addresses customer requirements
XML marker: <solution_overview>...</solution_overview>

SECTION 5 — Solution Architecture
Content: BLANK SECTION
Add heading: Solution Architecture
Add paragraph: "The solution architecture for [customer] is detailed below.
[PLACEHOLDER: Insert architecture diagram here]"
Add empty table with headers:
Component | Product | Role | Deployment Mode | Notes
Add 5 empty rows for manual completion
Add note: "[TO BE COMPLETED: Add architecture diagram and complete table]"

SECTION 6 — Product Descriptions
Model: RAG only — no AI generation for this section
RAG: For each selected product call search_products(product name, n=3)
Format each product as:
  - Bold product name as sub-heading
  - Retrieved RAG content formatted as paragraphs
  - Key features as bullet list if found in RAG content

SECTION 7 — Compliance Statement
Model: granite4.1:30b
Source: analysis requirements + selected products
Generate: Compliance statement table with columns:
  Req ID | Requirement | Compliance | Nexus Solution | Comments
  Mark MANDATORY rows, use statuses: Fully Compliant / Partially / TBC
XML marker: <compliance>...</compliance>

SECTION 8 — Technical Sizing
Content: BLANK SECTION
Add heading: Technical Sizing and Infrastructure Requirements
Add paragraph: "[PLACEHOLDER: Complete based on customer environment sizing]"
Add empty table with headers:
Component | Specification | Quantity | Notes
Rows for: Application Server, Database Server, HSM, Load Balancer,
  Storage, Network, High Availability
Add note: "[TO BE COMPLETED: Insert customer environment sizing]"

SECTION 9 — Scope of Work
Model: granite4.1:30b
Source: selected products + analysis requirements
Generate: Numbered list of deliverables and activities
Include: Supply, Install, Configure, Integrate, Test, Train, Go-live support
XML marker: <scope>...</scope>

SECTION 10 — Assumptions and Dependencies
Model: deepseek-r1:32b (load from OLLAMA_ANALYSIS_MODEL env var)
Source: analysis risk_areas + requirements
Generate: Numbered assumptions list + numbered dependencies list
XML marker: <assumptions>...</assumptions>

SECTION 11 — Implementation Approach
Model: granite4.1:30b
Generate: 4-phase implementation methodology:
  Phase 1: Project Initiation and Planning
  Phase 2: Installation and Configuration
  Phase 3: Integration and Testing
  Phase 4: Go-Live and Handover
For each phase: objectives, activities, deliverables, duration estimate
XML marker: <implementation>...</implementation>

SECTION 12 — Project Management
Model: granite4.1:30b
Generate: Project governance structure, RACI overview,
  communication plan, risk management approach, change management
XML marker: <project_mgmt>...</project_mgmt>

SECTION 13 — Support Model
Model: granite4.1:30b
Generate: Post-implementation support tiers:
  Standard Support: business hours, SLA details
  Premium Support: 24x7, SLA details
  Professional Services: on-demand, advisory
XML marker: <support>...</support>

SECTION 14 — Training
Model: granite4.1:30b
Generate: Training offerings:
  Administrator Training: duration, content, audience
  End User Training: duration, content, audience
  Technical Deep-dive: duration, content, audience
XML marker: <training>...</training>

SECTION 15 — Project Timeline
Content: BLANK SECTION
Add heading: Indicative Project Timeline
Add paragraph: "[PLACEHOLDER: Insert project timeline based on customer requirements]"
Add empty table with headers:
Phase | Activity | Duration | Start | End | Dependencies
Add 8 empty rows
Add note: "[TO BE COMPLETED: Confirm timeline with customer]"

SECTION 16 — Commercials
Content: BLANK SECTION
Add heading: Commercial Proposal
Add paragraph: "[PLACEHOLDER: Insert commercial pricing based on solution configuration]"
Add empty table with headers:
Item | Product/Service | Qty | Unit Price | Total | Notes
Add 10 empty rows
Add subtotal row
Add note: "[TO BE COMPLETED: Insert pricing from commercial team]"

SECTION 17 — Company Profile and References
RAG: search_proposals("Nexus PKI deployment customer reference", n=3)
+ search_industries(industry_vertical, n=2)
Generate: 1 paragraph Nexus company overview
Then: Customer References section with 3 reference profiles
  pulled from RAG content about past deployments
  Format: Industry | Solution Deployed | Scale | Outcome
XML marker: <company_profile>...</company_profile>

WORD DOCUMENT FORMATTING RULES:
- Page margins: 1 inch all sides
- Font: Calibri 11pt body, Calibri 14pt headings
- Heading 1: Dark blue #1F3864, bold, 14pt
- Heading 2: Dark blue #1F3864, bold, 12pt
- Table header rows: Dark blue fill #1F3864, white bold text
- Table alternating rows: light blue fill #DEEAF1 for even rows
- Footer: "Confidential — Nexus | {document title} | Page {n}"
- Header: Nexus logo placeholder + document title
- Auto page numbers in footer
- Page break before each major section (Heading 1)

After building proposal.py, update src/main.py to:
- Add phase 4 to the pipeline after phase 2 product selection
- Call proposal.generate_proposal() with analysis, products, output_dir, config
- Show proposal path in final output table
- The --phase flag: 1=Excel only, 2=Excel+Summary, 3=all three outputs

Do not modify any other files.
After completion confirm exactly what was built and what was changed.
```

---

## STEP 4 — Verify Build

Exit Claude Code then run:

```bash
wc -l src/proposal.py
grep "def " src/proposal.py
```

Expected: 300+ lines, 15+ functions visible.

---

## STEP 5 — Run Full Pipeline Test

Ensure Ollama is running:
```bash
ollama list
```

Run with your real RFP:
```bash
python src/main.py --rfp "data/rfp/RFQ2600170_Public_Key_Infrastructure.pdf"
```

### Expected Full Pipeline Output:
```
╔══════════════════════════════════════╗
║  PRESALES AI PLATFORM v0.4.0         ║
╚══════════════════════════════════════╝

📄 Step 1: Loading RFP...
   ✅ 47 pages, 14,200 words extracted

🧠 Step 2: Analyzing with qwq:latest...
   ✅ 34 requirements (22 mandatory, 12 optional)
   ✅ Industry: eGovernment
   ✅ Budget: USD 2-5 million

📊 Step 3: Compliance Excel generated
   ✅ output/compliance/RFQ_Compliance_20260610.xlsx

📋 Step 4: Displaying analysis results...
   [Shows requirements, evaluation criteria, win themes]

? Select products to propose: [interactive menu]
   ✅ 4 products selected

📝 Step 5: Generating customer summary...
   ✅ output/summaries/RFQ_Summary_20260610.docx

📄 Step 6: Generating proposal draft...
   🔍 Retrieving product knowledge from RAG...
   ✍️  Writing sections with qwen3.6:27b...
   ✅ output/proposals/RFQ_Proposal_Draft_20260610.docx

══════════════════════════════════════
  ALL OUTPUTS GENERATED
══════════════════════════════════════
  📊 Compliance:   output/compliance/xxx.xlsx
  📝 Summary:      output/summaries/xxx.docx
  📄 Proposal:     output/proposals/xxx.docx
══════════════════════════════════════
  Total time: ~8-12 minutes
```

---

## STEP 6 — Review Proposal Quality

```bash
# Open the generated proposal
open output/proposals/*.docx
```

Check each section:
```
[ ] Cover page has correct customer name and date
[ ] Executive summary is professional and relevant
[ ] Requirements table populated from RFP
[ ] Solution overview mentions selected products
[ ] Section 5 Architecture has blank table ready to fill
[ ] Product descriptions pulled from knowledge base
[ ] Compliance table populated with requirements
[ ] Section 8 Technical Sizing has blank table
[ ] SOW has relevant deliverables
[ ] Assumptions are logical for this type of project
[ ] Implementation phases make sense
[ ] Section 15 Timeline has blank table
[ ] Section 16 Commercials has blank table
[ ] Company profile references similar past deployments
```

---

## STEP 7 — Common Issues and Fixes

### Issue: Proposal generation times out
```bash
# In Claude Code say:
"The proposal generation is timing out on large sections.
Reduce each section prompt to maximum 500 words of context.
Use format_context(results, max_chars=2000) for RAG content.
Increase Ollama timeout to 400 seconds."
```

### Issue: Section content is generic
```bash
# In Claude Code say:
"Section [X] content is too generic. Add more context from
the analysis dict — include specific customer requirements,
industry vertical, and selected product names in the prompt."
```

### Issue: Word formatting looks wrong
```bash
# In Claude Code say:
"The Word document formatting needs fixing:
- Heading 1 should be dark blue #1F3864 not default blue
- Table headers need dark blue fill with white text
- Body text should be Calibri 11pt throughout
Fix only the formatting functions in proposal.py"
```

---

## STEP 8 — Commit Phase 4

```bash
cd ~/AI-Projects/presales-ai-platform

git add .
git status | grep -E "\.env$|\.pdf$"
# Must return nothing

git commit -m "feat: Phase 4 complete — full 17-section proposal generator

- src/proposal.py: complete Word proposal generator
- 17 sections: auto-generated + blank with tables for manual input
- RAG integration: product and industry knowledge retrieved per section
- Models: qwen3.6:27b (writing) + granite4.1:30b (compliance)
  + deepseek-r1:32b (assumptions and risk)
- Sections auto-filled: exec summary, requirements, solution overview,
  product descriptions, compliance, SOW, assumptions, implementation,
  PM, support, training, company profile
- Sections blank + table: architecture, sizing, timeline, commercials
- Full pipeline: RFP → Excel + Summary + Proposal in one command"

git push origin phase-4-proposal
git checkout main
git merge phase-4-proposal
git push origin main
git tag -a v0.4.0 -m "Phase 4: Full 17-section proposal generator complete"
git push origin v0.4.0
```

---

## Phase 4 Checklist

```
[ ] Git branch phase-4-proposal created
[ ] docs/plans/2026-06-10-phase4.md saved
[ ] Claude Code built proposal.py (300+ lines)
[ ] main.py updated with Phase 4 pipeline
[ ] Full pipeline runs without errors
[ ] Word document opens with all 17 sections
[ ] Auto sections have relevant AI-generated content
[ ] Blank sections have formatted empty tables
[ ] RAG content appears in product descriptions
[ ] Cover page shows correct customer name
[ ] Committed and pushed
[ ] Merged to main
[ ] v0.4.0 tag created
```

---

## After Phase 4 — LinkedIn Post

```
📄 Phase 4 shipped — Presales AI Platform now generates 
complete 17-section proposal drafts.

One command now produces:
📊 Compliance Excel matrix
📝 Customer summary document  
📄 17-section Word proposal draft

Auto-generated sections use my local knowledge base
of 11 Nexus products and 10 industry verticals.

Blank sections (architecture, sizing, timeline, commercials)
have pre-formatted tables ready to fill in.

From RFP to proposal skeleton in under 12 minutes.

GitHub: github.com/cartertan/presales-ai-platform

#AIArchitect #LocalAI #PresalesAI #BuildInPublic #PKI
```

---

*Carter Tan · AI Architect Journey · Phase 4 Guide · 10 June 2026*
