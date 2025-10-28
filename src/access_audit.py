import pandas as pd, json, os

policy_path = "data/IT_RBAC_Matrix_SAMPLE.xlsx"
actual_path = "data/actual_access_SAMPLE.json"

if not (os.path.exists(policy_path) and os.path.exists(actual_path)):
    raise FileNotFoundError("❌ Missing policy or actual access files. Run mock_data_generator.py first.")

df_policy = pd.read_excel(policy_path)
with open(actual_path) as f:
    actual_data = json.load(f)
df_actual = pd.DataFrame(actual_data)

findings = []

for _, row in df_actual.iterrows():
    user, system, role = row["user"], row["system"], row["role"]
    expected_roles = df_policy[df_policy["System"] == system]["Expected Access"].tolist()

    if not expected_roles:
        findings.append({"user": user, "system": system, "issue": "Unknown System"})
    elif role not in expected_roles:
        findings.append({"user": user, "system": system, "issue": f"Unexpected Role: {role}"})

df_findings = pd.DataFrame(findings)
df_findings.to_csv("data/drift_report.csv", index=False)
print("✅ Drift audit completed. Results saved to data/drift_report.csv")
