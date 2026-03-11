import os
from datetime import datetime


def show_dashboard():

    print("\n=========== Backup Dashboard ===========")

    log_file = "logs/backup_log.txt"

    if os.path.exists(log_file):

        with open(log_file, "r") as f:

            lines = f.readlines()

            print("Last 5 backup events:\n")

            for line in lines[-5:]:
                print(line.strip())

    else:
        print("No logs found.")

    print("\nDashboard updated at:", datetime.now())
    print("========================================\n")