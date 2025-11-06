# CRM Automation Script & Data Extraction

**Company:** The Knot Worldwide  
**Project:** CRM Automation Script & Data Extraction  
**Duration:** Dec 2024 – Feb 2025

## Overview
This repository contains code, documentation, and sample data demonstrating CRM automation used to:
- Bulk update CRM fields (emails, ZIP codes) via VBA and exported CSVs.
- Validate and enrich vendor contact data using Python + Google APIs.
- Extract vendor website URLs from social media text using OpenAI (example usage).
- Provide reproducible examples of validation, enrichment, and reporting pipelines.

> ⚠️ This repository contains sample and anonymized data only. Replace sample files with production data and credentials as needed.

---

## Repo Structure

```
crm-automation-tkww/
├─ README.md
├─ LICENSE
├─ .gitignore
├─ requirements.txt
├─ sample_data/
│  └─ contacts_sample.csv
├─ src/
│  ├─ validate_contacts.py
│  ├─ enrich_with_google_api.py
│  └─ openai_extractor.py
├─ vba/
│  └─ crm_bulk_update.bas
└─ docs/
   └─ workflow_diagram.png
```

---

## How to use

### Python environment (recommended)
1. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate    # macOS/Linux
venv\\Scripts\\activate     # Windows
pip install -r requirements.txt
```

2. Validate sample contacts:
```bash
python src/validate_contacts.py sample_data/contacts_sample.csv
```

3. Enrich with Google API (requires API key and enabling appropriate Google services):
```bash
python src/enrich_with_google_api.py sample_data/contacts_sample.csv
```

4. OpenAI extraction (requires OPENAI_API_KEY in environment):
```bash
export OPENAI_API_KEY="your_key_here"
python src/openai_extractor.py sample_data/contacts_sample.csv
```

---

## Files of interest

- `src/validate_contacts.py` — Validate emails & phone numbers and produce a cleaned CSV.
- `src/enrich_with_google_api.py` — Example wrapper for Google Places / Knowledge Graph API calls.
- `src/openai_extractor.py` — Illustrative example of using OpenAI to parse unstructured social text to extract candidate URLs.
- `vba/crm_bulk_update.bas` — VBA macro code snippet for bulk updates in CRM via Excel.
- `sample_data/contacts_sample.csv` — Small anonymized dataset for testing.

---

## Notes & Security
- Do **not** commit API keys or production data to the repository.
- Use `.env` or secret management for credentials.
- Thoroughly test scripts on small anonymized datasets before running in production.

---

If you'd like, I can:
- Add a Jupyter notebook demoing the validation pipeline,
- Create GitHub Actions to run basic linting and tests,
- Or produce a short demo GIF showing the VBA bulk upload and Python validation workflow.
