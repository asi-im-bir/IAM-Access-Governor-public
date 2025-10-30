#🔒 IAM Access Governor

Automated Identity & Access Governance for Continuous Zero Trust Compliance

A Python-based solution that continuously verifies user access, detects privilege drift, and produces audit-ready compliance reports aligned with NIS2 and ISO/IEC 27001.

🚀 Project Summary

Modern organizations often manage access manually — through spreadsheets, tickets, or quarterly reviews.
This leads to privilege drift and compliance gaps.

IAM Access Governor turns IAM governance into a continuous, data-driven control by comparing declared RBAC policy against actual system access every day.

## ⚙️ Key Features

| Feature | Description |
|----------|-------------|
| **Automated Drift Detection** | Compares policy (Excel) vs. actual access (JSON) |
| **Matrix RBAC Analysis** | Works with matrix-style Excel (Employee × System Access) |
| **Proactive Risk Discovery** | Detects excessive privileges or mismatched roles |
| **Compliance-ready Reports** | Exports findings as CSV + color-coded HTML |
| **Human Skepticism Encoded** | Automates “trust but verify” principle in access control |
| **No Cloud Dependency** | Fully local, no external API or AI service needed |

🧩 How It Works
flowchart LR
    A[RBAC Policy Matrix (Excel)] --> B[access_audit.py<br>Compare Policy vs Actual Access]
    C[Actual Access (JSON Snapshot)] --> B
    B --> D[drift_report.csv<br>Detected Privilege Drift]
    D --> E[drift_logger.py<br>Audit Log]
    D --> F[report_generator.py<br>Visual Report]
    E --> G[drift_log.json]
    F --> H[drift_report.html<br>Compliance Dashboard]


Workflow:
1️⃣ Generate or import RBAC policy and access data
2️⃣ Audit automatically → detect mismatches or excessive privileges
3️⃣ Log every drift → produce visual and audit-ready reports
4️⃣ Integrate findings into GRC systems (Slack, Jira, SIEM)

📊 Example Output
User	System	Finding	Expected	Actual	Severity	Date
ahmet	AWS Cloud	Excessive Privilege	Read	Admin	High	2025-10-28
ayse	Jira	Access Missing	Read, Write	None	Medium	2025-10-28

🔹 Drift_report.html — color-coded dashboard for management
🔹 Drift_log.json — timestamped audit trail (for ISO/NIS2 evidence)


🛡️ Compliance Alignment
Framework	Requirement	Implementation
NIS2 Art. 21(2)(c)	Access control & asset management	Continuous IAM drift monitoring
ISO 27001 A.9.2.6	Removal of access upon change	Detects orphaned or expired privileges
ISO 27001 A.10.1.1	Logging & monitoring	Structured JSON/CSV audit logs
ISO 27001 A.5.30	ICT readiness	Nightly verification loop (CI/CD-ready)

---

## 🧠 Architecture Overview

```plaintext
                   ┌────────────────────────┐
                   │  IT_RBAC_Matrix_.xlsx  │
                   │  (RBAC Policy Matrix)   │
                   └──────────┬─────────────┘
                              │
                              ▼
                 ┌────────────────────────────┐
                 │ mock_data_generator.py      │
                 │ → Generates actual_access.json │
                 └──────────┬─────────────┘
                              │
                              ▼
                 ┌────────────────────────────┐
                 │ access_audit.py            │
                 │ → Compares RBAC vs actual  │
                 │ → Creates drift_report.csv │
                 └──────────┬─────────────┘
                              │
                              ▼
                 ┌────────────────────────────┐
                 │ drift_logger.py            │
                 │ → Logs findings in JSON    │
                 └──────────┬─────────────┘
                              │
                              ▼
                 ┌────────────────────────────┐
                 │ report_generator.py        │
                 │ → Generates HTML Dashboard │
                 └────────────────────────────┘
🧩 File Structure
IAM Access Governor/
│
├── data/
│   ├── IT_RBAC_Matrix_.xlsx       # Policy source
│   ├── actual_access.json          # Generated mock access data
│   ├── drift_report.csv            # Audit output
│   ├── drift_log.json              # Change history
│   └── drift_report.html           # Visual dashboard
│
├── src/
│   ├── mock_data_generator.py
│   ├── access_audit.py
│   ├── drift_logger.py
│   └── report_generator.py
│
├── docs/
│   └── architecture.png            # (optional diagram export)
│
├── requirements.txt
└── README.md

🧰 Setup & Usage
1️⃣ Clone the Repository
git clone https://github.com/asi-im-bir/IAM-Access-Governor.git
cd IAM-Access-Governor

2️⃣ Set Up Virtual Environment
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

3️⃣ Generate Mock Data
python src/mock_data_generator.py

4️⃣ Run Audit & Reports
python src/access_audit.py
python src/drift_logger.py
python src/report_generator.py

5️⃣ View the Report

Open:

data/drift_report.html


🔎 Example Output
User	System	Finding	Expected	Actual	Severity	Date
ahmet	Cloud Infrastructure	Excessive privilege	Not Admin	Admin	High	2025-10-25
ayse	DNS Management	Access mismatch	Read, Write	None	Medium	2025-10-25

---

🧠 Real-World Challenge Addressed
Problem: Privilege drift and exception mismanagement across hybrid systems.
Risks:

Outdated admin access → insider threats

Expired exceptions → NIS2 non-compliance

No traceability → failed ISO 27001 audit

IAM Access Governor Solution:

Challenge	Project Function	Output
Uncontrolled privilege creep	Automated policy-to-access drift detection	drift_report.csv
Expired elevated access	Exception expiry detection	drift_log.json
Missing evidence	Continuous audit trail generation	drift_report.html
Manual IAM review	Script-based, repeatable verification	GitHub Actions-ready pipeline

🔮 Future Enhancements
Enhancement	Description	Impact
🔁 GitHub Actions / Cron Automation	Schedule nightly drift audits to maintain continuous verification.	Enables continuous compliance without human intervention.
🧩 Live API Connectors (AD, Azure, AWS, Jira)	Replace mock data with live IAM integrations.	Real-time access validation across hybrid systems.
📡 Slack / Jira Integration	Send high-severity drift alerts or create auto-tickets.	Closes the loop between detection and remediation.
🧠 ML-Based Anomaly Detection	Learn normal access patterns per team to flag anomalies.	Predictive IAM analytics — from detection to prevention.
🧾 Policy-as-Code (YAML)	Convert RBAC matrices into version-controlled YAML definitions.	Enables DevSecOps-friendly, auditable access governance.
📈 SIEM / GRC Integration	Push evidence and drift data to Splunk, Conformio, or Archer dashboards.	Unified IAM risk visualization across the enterprise.

🎯 Summary for Hiring Managers

IAM Access Governor is a Python-based tool that automatically checks and verifies user access across systems.
It detects excessive or missing permissions by comparing policy (Excel) with real access data (JSON) — then generates clear reports for audits and compliance.
This project automates manual access reviews, reduces risk, and provides continuous, evidence-based compliance with NIS2 and ISO 27001.


