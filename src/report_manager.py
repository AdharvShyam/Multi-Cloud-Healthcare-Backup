class BackupReport:

    def __init__(self):
        self.total_files = 0
        self.local_success = 0
        self.cloud_success = 0
        self.retry_success = 0
        self.failover_count = 0

    def print_report(self):

        print("\nBackup Summary")
        print("--------------")

        print(f"Total Files Processed: {self.total_files}")
        print(f"Local Backups: {self.local_success}")
        print(f"Cloud Uploads: {self.cloud_success}")
        print(f"Retries: {self.retry_success}")
        print(f"Failovers Triggered: {self.failover_count}")