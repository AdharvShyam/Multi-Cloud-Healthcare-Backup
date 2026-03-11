import os
import shutil
from datetime import datetime

from src.file_manager import get_all_files
from src.cloud_uploader import upload_file
from src.logger import log_event


DATA_FOLDER = "data/healthcare_data"
LOCAL_BACKUP_FOLDER = "backup/local_backup"


def perform_backup():

    print("Starting Healthcare Backup Process...\n")

    files = get_all_files(DATA_FOLDER)

    if not os.path.exists(LOCAL_BACKUP_FOLDER):
        os.makedirs(LOCAL_BACKUP_FOLDER)

    for file_path in files:

        try:

            file_name = os.path.basename(file_path)

            # Step 1 — Local Backup
            backup_path = os.path.join(LOCAL_BACKUP_FOLDER, file_name)
            shutil.copy(file_path, backup_path)

            log_event(f"Local backup successful: {file_name}")
            print(f"Local Backup Done: {file_name}")

            # Step 2 — Cloud Backup
            upload_file(file_path)

            log_event(f"Cloud backup successful: {file_name}")

        except Exception as e:

            log_event(f"Backup FAILED for {file_path} : {str(e)}")
            print(f"Backup failed for {file_path}")