# VarshithNV_HighBar_V2
High Bar V2 Assignment – Applied AI Engineer | Kasparro Production-grade Agentic FB Ads Analytics Pipeline – Schema Validation, Drift Detection, Observability, Confidence Scoring
# High Bar V2 — Production-grade Agentic FB Ads Analytics Pipeline  
Applied AI Engineer Assignment — Kasparro

This project demonstrates end-to-end ownership of a small production-style system for diagnosing Facebook ads performance, identifying drivers of change, validating hypotheses with evidence, and generating targeted creative recommendations.

The system is designed for real-world reliability, including:
- Schema validation
- Drift detection
- Confidence scoring
- Error handling
- Observability & JSON logs
- Developer-friendly execution

---

## 🔧 V2 Architecture (Production Thinking)

Data → Insight → Evidence → Validation → Creative Generation → Report

| Component | Responsibility |
|----------|----------------|
| Data Loader | Load CSV, validate schema, drift detection |
| Insight Engine | Segment, compare baselines, detect drops & opportunities |
| Evaluator | Severity score, confidence score, evidence JSON |
| Creative Engine | Generate creatives tied to exact performance drivers |
| Logger | JSON logs per run (decisions + errors + evidence) |
| Config | Thresholds & schema defined in YAML |
| Tests | Unit & pipeline correctness |
| Reports | Output insights + creatives in structured JSON |

---
VarshithNV_HighBar_V2
┣ src/
┃ ┣ agents/ # planner, data loader, insight engine, creative generator
┃ ┣ evaluator/ # confidence scoring, validation
┃ ┣ utils/ # logging, helpers
┣ logs/ # JSON logs per run
┣ config/ # config.yaml (schema + thresholds)
┣ data/ # dataset
┣ reports/ # final structured insights + creatives
┣ tests/ # unit + edge case tests
┗ README.md




---

## 🧪 Key V2 Enhancements

- Added explicit schema validation
- Added schema drift warnings
- Added confidence & severity scoring
- Introduced decision logging (JSON)
- JSON logs stored by timestamp
- Config-driven thresholds (no magic numbers)
- Added basic unit tests
- Improved developer experience workflow

---

## 🛠 Setup & Run

### Install dependencies


pip install -r requirements.txt


### Run pipeline


python src/run.py


### Run tests


pytest


---

## ✨ Output Deliverables

| File | Description |
|------|------------|
| /reports/insights.json | Drivers of performance change |
| /reports/creatives.json | Targeted ads creatives |
| /reports/metrics.json | Baseline, deltas, scoring |
| /logs/*.json | All decisions, errors, outcomes |

---

## 👤 Author
**Varshith N V**  
High Bar V2 Submission — Applied AI Engineer 
## 📁 Repository Structure

