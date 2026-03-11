# Multi-Cloud Hybrid Strategy for Healthcare

## Project Overview

This project is about keeping healthcare data safe by storing it in places. We use Python to simulate a system that backs up healthcare data in storage locations. This way we can keep data safe and systems reliable.

The system stores healthcare files in both storage and cloud storage. This is done to make sure data is always available.

## Objectives

- Create a system that backs up healthcare data
- Use Python to back up data from sources
- Show how to keep data safe with redundancy and failover methods
- Keep data safe with both local and cloud storage

## Technologies Used

- Python
- Google Drive API
- Local Storage
- Git & GitHub
- VS Code

## Project Structure

```
MultiCloud-Healthcare-Backup
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
│
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

- Automatic backup of healthcare files
- Backup data from many sources (local and cloud)
- Use Google Drive API to store data in the cloud
- Check if data is correct using SHA256 Hash
- Try again if cloud upload fails
- Keep data safe if cloud backup fails
- Record all backup actions
- Show backup status on a dashboard
- Schedule backups to run automatically

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
Check if data is correct     Upload Manager
(SHA256 Hash)                     │
│                               │
└───────────────┬───────────────┘
▼
Try again if upload fails
│
▼
Keep data safe if fails
│
▼
Backup Logs + Dashboard
```

## How the Backup System Works

1. Healthcare CSV files are stored in the dataset folder.
2. The Python backup engine scans all healthcare files.
3. Each file is copied to the backup directory.
4. A SHA256 hash is generated to check if data's correct.
5. Files are uploaded to Google Drive using the Drive API.
6. If the cloud upload fails the system tries again.
7. If it still fails the system keeps data safe locally.
8. All actions are recorded in the log file.
9. The dashboard shows backup events.
10. The scheduler can run backups automatically at set times.

## Learning Outcomes

This project helps you understand:

- How to keep data with cloud computing
- Data redundancy
- Failover systems
- Cloud API integration

## Future Enhancements

- Integration with AWS S3
- Encryption for sensitive healthcare data
- Automated scheduled backups
- Web dashboard, for monitoring backups

## How to Run the Project

1. Clone the repository

```
git clone https://github.com/AdharvShyam/Multi-Cloud-Healthcare-Backup.git
```

2. Install dependencies

```
pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib schedule
```

3. Generate healthcare dataset

```
python generate_healthcare_data.py
```

4. Run the backup system

```
python main.py
```

## Dataset

The project uses a simulated healthcare dataset that includes:

- Patient records
- Appointment data
- Lab reports
- Prescription records

The dataset is automatically created using the script:

```
generate_healthcare_data.py
```

## Author

Adharv Shyam  
BCA Final Year Project
