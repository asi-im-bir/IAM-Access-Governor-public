import pandas as pd, json, os

os.makedirs("data", exist_ok=True)

# Mock RBAC Policy-as-Code (Source of Truth)
policy_data = {
    "System": ["AWS", "GitHub", "JIRA"],
    "Group": ["Developers", "SRE", "Finance"],
    "Expected Access": [
        "AWS:Developer-ReadOnly",
        "AWS:SRE-Admin",
        "JIRA:Finance-ReadOnly"
    ]
}
pd.DataFrame(policy_data).to_excel("data/IT_RBAC_Matrix_SAMPLE.xlsx", index=False)

# Mock Actual Access State (JSON)
actual_access = [
    {"user": "alice.dev", "system": "AWS", "role": "Developer-ReadOnly"},
    {"user": "bob.sre", "system": "AWS", "role": "AdministratorAccess"},  # drift
    {"user": "carol.finance", "system": "JIRA", "role": "Finance-ReadOnly"},
    {"user": "dave.intern", "system": "JIRA", "role": "jira-sre-admins"}   # drift
]
with open("data/actual_access_SAMPLE.json", "w") as f:
    json.dump(actual_access, f, indent=4)

print("✅ Mock data generated successfully!")
