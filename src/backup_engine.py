import os
import shutil

from src.file_manager import get_all_files, get_file_hash
from src.cloud_uploader import upload_file  # Google Drive
from src.s3_uploader import upload_to_s3   # AWS S3
from src.logger import log_event
from src.report_manager import BackupReport


DATA_FOLDER = "data/healthcare_data"
LOCAL_BACKUP_FOLDER = "backup/local_backup"


def perform_backup():

    print("Starting Healthcare Backup Process...\n")

    report = BackupReport()

    files = get_all_files(DATA_FOLDER)

    if not os.path.exists(LOCAL_BACKUP_FOLDER):
        os.makedirs(LOCAL_BACKUP_FOLDER)

    for file_path in files:

        report.total_files += 1
        file_name = os.path.basename(file_path)

        backup_path = os.path.join(
            LOCAL_BACKUP_FOLDER,
            file_name
        )

        try:
            # ---------------------------
            # LOCAL BACKUP
            # ---------------------------
            shutil.copy(file_path, backup_path)

            log_event(f"Local backup successful: {file_name}")
            report.local_success += 1

            # ---------------------------
            # INTEGRITY CHECK (SHA256)
            # ---------------------------
            original_hash = get_file_hash(file_path)
            backup_hash = get_file_hash(backup_path)

            if original_hash == backup_hash:
                log_event(f"Integrity check passed for {file_name}")
            else:
                log_event(f"Integrity check FAILED for {file_name}")

            # ---------------------------
            # SIZE VERIFICATION
            # ---------------------------
            if os.path.getsize(file_path) == os.path.getsize(backup_path):
                log_event(f"Backup verification passed for {file_name}")
            else:
                log_event(f"Backup verification FAILED for {file_name}")

            # ---------------------------
            # CLOUD BACKUP FLAGS
            # ---------------------------
            google_success = False
            s3_success = False

            # ---------------------------
            # GOOGLE DRIVE BACKUP
            # ---------------------------
            try:
                upload_file(file_path)
                log_event(f"Google Drive backup successful: {file_name}")
                report.cloud_success += 1
                google_success = True

            except Exception as drive_error:
                log_event(
                    f"Google Drive failed for {file_name}: {drive_error}"
                )

            # ---------------------------
            # AWS S3 BACKUP
            # ---------------------------
            try:
                upload_to_s3(file_path)
                log_event(f"AWS S3 backup successful: {file_name}")
                report.cloud_success += 1
                s3_success = True

            except Exception as s3_error:
                log_event(
                    f"AWS S3 failed for {file_name}: {s3_error}"
                )

            # ---------------------------
            # FAILOVER
            # ---------------------------
            if not google_success and not s3_success:
                log_event(
                    f"Failover triggered for {file_name}. "
                    f"Data retained locally."
                )
                report.failover_count += 1

        except Exception as backup_error:
            log_event(
                f"Backup FAILED for {file_name}: {backup_error}"
            )

    # ---------------------------
    # FINAL REPORT
    # ---------------------------
    report.print_report()