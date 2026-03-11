import os
from datetime import datetime

LOG_FILE = "logs/backup_log.txt"


def log_event(message):

    if not os.path.exists("logs"):
        os.makedirs("logs")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_message = f"[{timestamp}] {message}\n"

    with open(LOG_FILE, "a") as log_file:
        log_file.write(log_message)

    print(f"LOG: {message}")