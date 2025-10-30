
# 🔒 IAM Access Governor

### **Automated Identity & Access Governance for Continuous Zero Trust Compliance**

> **A Python-based solution** that continuously verifies user access, detects privilege drift, and generates audit-ready compliance reports aligned with **NIS2** and **ISO/IEC 27001**.

---

## 🚀 Project Summary

Most organizations still manage access manually — through spreadsheets, tickets, or quarterly reviews.
This creates **privilege drift**, **excessive privileges**, and **compliance gaps**.

**IAM Access Governor** turns access governance into a **continuous, data-driven control**, comparing declared RBAC policies against actual system access — **every day**.

> 🧠 *“Don’t trust what’s declared — verify what’s real.”*

---

## ⚙️ Key Features

| Feature                       | Description                                                     |
| ----------------------------- | --------------------------------------------------------------- |
| **Automated Drift Detection** | Compares declared RBAC policy (Excel) vs. actual access (JSON). |
| **Matrix RBAC Analysis**      | Supports Excel-based Employee × System Access matrix.           |
| **Proactive Risk Discovery**  | Detects excessive privileges and role mismatches.               |
| **Compliance-Ready Reports**  | Exports CSV + color-coded HTML reports.                         |
| **Built-In Audit Trail**      | Logs every drift with timestamp and severity.                   |
| **No Cloud Dependency**       | 100% local execution — no external APIs or services.            |

---

## 🧩 How It Works

### Workflow

1️⃣ Import or generate RBAC policy (`.xlsx`) and actual access data (`.json`).
2️⃣ Run audit (`access_audit.py`) to detect mismatches or excessive privileges.
3️⃣ Log each drift (`drift_logger.py`) and generate audit-ready reports (`report_generator.py`).
4️⃣ Integrate findings with **Slack**, **Jira**, or **SIEM** for remediation.

---

## 📊 Example Output

| User  | System    | Finding             | Expected    | Actual | Severity  | Date       |
| ----- | --------- | ------------------- | ----------- | ------ | --------- | ---------- |
| ahmet | AWS Cloud | Excessive Privilege | Read        | Admin  | 🔴 High   | 2025-10-28 |
| ayse  | Jira      | Access Missing      | Read, Write | None   | 🟠 Medium | 2025-10-28 |

**Generated Artifacts:**

* 🧾 `drift_report.html` — Color-coded management dashboard
* 📜 `drift_log.json` — Timestamped audit trail for ISO/NIS2 evidence

---

## 🛡️ Compliance Alignment

| Framework              | Requirement                       | Implementation                          |
| ---------------------- | --------------------------------- | --------------------------------------- |
| **NIS2 Art. 21(2)(c)** | Access control & asset management | Continuous IAM drift monitoring         |
| **ISO 27001 A.9.2.6**  | Removal of access upon change     | Detects orphaned or expired privileges  |
| **ISO 27001 A.10.1.1** | Logging & monitoring              | Structured JSON/CSV audit logs          |
| **ISO 27001 A.5.30**   | ICT readiness                     | Nightly verification loop (CI/CD-ready) |

---

## 🧠 Architecture Overview

```
┌────────────────────────┐
│  IT_RBAC_Matrix_.xlsx  │   →  RBAC Policy Matrix
└──────────┬─────────────┘
           │
           ▼
┌────────────────────────────┐
│ mock_data_generator.py     │ → Generates actual_access.json
└──────────┬─────────────┘
           │
           ▼
┌────────────────────────────┐
│ access_audit.py            │ → Compares RBAC vs actual
│                            │ → Creates drift_report.csv
└──────────┬─────────────┘
           │
           ▼
┌────────────────────────────┐
│ drift_logger.py            │ → Logs findings in JSON
└──────────┬─────────────┘
           │
           ▼
┌────────────────────────────┐
│ report_generator.py        │ → Generates HTML dashboard
└────────────────────────────┘
```

---

## 📁 File Structure

```
IAM Access Governor/
│
├── data/
│   ├── IT_RBAC_Matrix_.xlsx       # Policy source
│   ├── actual_access.json          # Generated mock access data
│   ├── drift_report.csv            # Audit results
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
│   └── architecture.png
│
├── requirements.txt
└── README.md
```

---

## 🧰 Setup & Usage

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/asi-im-bir/IAM-Access-Governor.git
cd IAM-Access-Governor
```

### 2️⃣ Create Virtual Environment & Install Dependencies

```bash
python -m venv .venv

# Activate
.venv\Scripts\activate    # Windows
source .venv/bin/activate # macOS/Linux

pip install -r requirements.txt
```

### 3️⃣ Generate Mock Data

```bash
python src/mock_data_generator.py
```

### 4️⃣ Run Full Audit Pipeline

```bash
python src/access_audit.py
python src/drift_logger.py
python src/report_generator.py
```

### 5️⃣ View Results

Open **`data/drift_report.html`** in your browser to see the compliance dashboard.

---

## ⚠️ Problem Solved

**Challenge:** Manual IAM reviews cause privilege drift, outdated admin access, and compliance risk.
**Solution:** IAM Access Governor automates access verification and continuous compliance.

✅ Continuous detection of access mismatches
✅ Automated, timestamped audit logs
✅ Clear, HTML-based compliance reporting

---

## 🔮 Future Enhancements

| Enhancement                               | Description                                   | Impact                                    |
| ----------------------------------------- | --------------------------------------------- | ----------------------------------------- |
| 🔁 **Automation (GitHub Actions / Cron)** | Schedule nightly audits                       | Continuous compliance without human input |
| 🧩 **API Connectors (AD, Azure, AWS)**    | Replace mock data with live integrations      | Real-time access validation               |
| 📡 **Slack / Jira Integration**           | Send alerts or auto-create tickets            | Fast incident response                    |
| 🧠 **ML-Based Anomaly Detection**         | Learn normal access patterns                  | Predictive, risk-based IAM control        |
| 🧾 **Policy-as-Code (YAML)**              | Convert Excel RBAC to version-controlled YAML | DevSecOps-ready governance                |
| 📈 **SIEM / GRC Integration**             | Export logs to Splunk, Conformio              | Unified compliance dashboard              |


## 🎯 Summary for Hiring Managers

**IAM Access Governor** is a **Python-based automation tool** that continuously verifies user access across systems.
It identifies excessive or missing permissions by comparing **policy (Excel)** with **real access (JSON)** — and generates **audit-ready visual reports**.

This project demonstrates:

* Automation of IAM governance
* Continuous compliance validation
* Evidence-based reporting for ISO/NIS2
---



---
