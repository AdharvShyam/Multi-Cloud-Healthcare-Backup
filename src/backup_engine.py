import os
import shutil

from src.file_manager import get_all_files, get_file_hash
from src.cloud_uploader import upload_file
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

            # LOCAL BACKUP
            shutil.copy(file_path, backup_path)

            log_event(f"Local backup successful: {file_name}")
            report.local_success += 1

            # DATA INTEGRITY CHECK (SHA256)
            original_hash = get_file_hash(file_path)
            backup_hash = get_file_hash(backup_path)

            if original_hash == backup_hash:
                log_event(f"Integrity check passed for {file_name}")
            else:
                log_event(f"Integrity check FAILED for {file_name}")

            # FILE SIZE VERIFICATION
            original_size = os.path.getsize(file_path)
            backup_size = os.path.getsize(backup_path)

            if original_size == backup_size:
                log_event(f"Backup verification passed for {file_name}")
            else:
                log_event(f"Backup verification FAILED for {file_name}")

            # CLOUD BACKUP
            try:

                upload_file(file_path)

                log_event(f"Cloud backup successful: {file_name}")
                report.cloud_success += 1

            except Exception as cloud_error:

                log_event(
                    f"Cloud backup failed for {file_name}: {cloud_error}"
                )

                # RETRY CLOUD UPLOAD
                try:

                    upload_file(file_path)

                    log_event(
                        f"Retry upload successful for {file_name}"
                    )

                    report.retry_success += 1

                except Exception:

                    log_event(
                        f"Failover triggered for {file_name}. "
                        f"Data retained in local backup."
                    )

                    report.failover_count += 1

        except Exception as backup_error:

            log_event(
                f"Backup FAILED for {file_name}: {backup_error}"
            )

    report.print_report()