import schedule, time, os

def run_audit_cycle():
    print("🚀 Running daily IAM Access Governor audit...")
    os.system("python src/access_audit.py")
    os.system("python src/drift_logger.py")
    os.system("python src/report_generator.py")

schedule.every().day.at("01:00").do(run_audit_cycle)

print("🕐 Scheduler active — running daily drift detection at 01:00")
while True:
    schedule.run_pending()
    time.sleep(60)
