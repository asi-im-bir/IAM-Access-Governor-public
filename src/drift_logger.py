import pandas as pd, datetime, os

report_path = "data/drift_report.csv"
log_path = "data/drift_log.json"

if not os.path.exists(report_path):
    raise FileNotFoundError("❌ No drift_report.csv found. Run access_audit.py first.")

df = pd.read_csv(report_path)
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
df["timestamp"] = timestamp

df.to_json(log_path, orient="records", indent=4)
print(f"✅ Drift log updated → {log_path}")
