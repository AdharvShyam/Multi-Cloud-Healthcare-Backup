import schedule
import time
from datetime import datetime
from src.backup_engine import perform_backup
from src.dashboard import show_dashboard


def run_backup():

    print("\n==============================")
    print("Healthcare Backup System")
    print("Backup started at:", datetime.now())
    print("==============================\n")

    perform_backup()
    show_dashboard()

    print("\nBackup completed.\n")


# Run backup every 10 minutes
schedule.every(10).minutes.do(run_backup)

print("Backup scheduler started...")
print("Backups will run every 10 minutes.\n")

# Run once immediately
run_backup()

while True:
    schedule.run_pending()
    time.sleep(1)