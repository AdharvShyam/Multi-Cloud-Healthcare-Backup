# Multi-Cloud Hybrid Strategy for Healthcare

## Project Overview
This project simulates a multi-cloud backup strategy for healthcare data using Python.  
It demonstrates how critical healthcare documents can be backed up across multiple storage locations to ensure data safety and system reliability.

The system implements redundancy and failover mechanisms by storing healthcare files in both local storage and cloud storage.

## Objectives
- Simulate a healthcare data backup system
- Implement multi-source backup using Python
- Demonstrate redundancy and failover concepts
- Ensure data safety using local and cloud storage

## Technologies Used
- Python
- Google Drive API
- Local Storage
- Git & GitHub
- VS Code

## Project Structure

```
Multi-Cloud-Healthcare-Backup
│
├── backup
│   └── local_backup
│
├── config
│
├── data
│   └── healthcare_data
│
├── logs
├── src
│   ├── backup_engine.py
│   ├── cloud_uploader.py
│   ├── file_manager.py
│   ├── logger.py
│   ├── dashboard.py
│   └── report_manager.py
│
├── main.py
├── README.md
├── LICENSE
└── .gitignore
```

## Key Features

• Automated Healthcare File Backup  
• Multi-Source Backup (Local + Cloud)  
• Google Drive API Integration  
• Data Integrity Verification (SHA256 Hash Check)  
• Retry Mechanism for Failed Cloud Uploads  
• Failover System if Cloud Backup Fails  
• Backup Logging System  
• Backup Status Dashboard (CLI)  
• Automated Backup Scheduler

## System Architecture

```
                Healthcare Dataset
                   (CSV Files)
                        │
                        ▼
                Backup Engine (Python)
                        │
        ┌───────────────┴───────────────┐
        │                               │
        ▼                               ▼
   Local Backup Folder            Cloud Backup
   (backup/local_backup)       (Google Drive API)
        │                               │
        │                               │
   Data Integrity Check           Upload Manager
      (SHA256 Hash)                     │
        │                               │
        └───────────────┬───────────────┘
                        ▼
                Retry Mechanism
                        │
                        ▼
                 Failover System
                        │
                        ▼
             Backup Logs + Dashboard
```

## How the Backup System Works

1. Healthcare CSV files are stored in the dataset folder.
2. The Python backup engine scans all healthcare files.
3. Each file is copied to the local backup directory.
4. A SHA256 hash is generated to verify file integrity.
5. Files are uploaded to Google Drive using the Drive API.
6. If cloud upload fails, the system retries automatically.
7. If the retry fails, the failover system ensures data remains safely stored locally.
8. All operations are logged in the backup log file.
9. The CLI dashboard displays recent backup events.
10. The scheduler can automatically run backups at fixed intervals.

## Learning Outcomes
This project helps understand:
- Cloud computing reliability
- Data redundancy
- Failover systems
- Cloud API integration

## Future Enhancements
- Integration with AWS S3
- Encryption for sensitive healthcare data
- Automated scheduled backups
- Web dashboard for monitoring backups

## How to Run the Project

1. Clone the repository

git clone https://github.com/AdharvShyam/Multi-Cloud-Healthcare-Backup.git

2. Install dependencies

pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib schedule

3. Generate healthcare dataset

python generate_healthcare_data.py

4. Run the backup system

python main.py

## Dataset

The project uses a simulated healthcare dataset consisting of:

• Patient records  
• Appointment data  
• Lab reports  
• Prescription records  

The dataset is automatically generated using the script:

generate_healthcare_data.py

## Author
Adharv Shyam  
BCA Final Year Project
