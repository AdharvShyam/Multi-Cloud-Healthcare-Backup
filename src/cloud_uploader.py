import os
import pickle

from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


SCOPES = ['https://www.googleapis.com/auth/drive.file']


def authenticate_drive():

    creds = None

    if os.path.exists('config/token.pickle'):
        with open('config/token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:

        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())

        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'config/credentials.json',
                SCOPES
            )

            creds = flow.run_local_server(port=0)

        with open('config/token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)

    return service


def get_backup_folder(service):

    folder_name = "Healthcare_Backups"

    query = f"name='{folder_name}' and mimeType='application/vnd.google-apps.folder'"

    results = service.files().list(q=query, fields="files(id, name)").execute()

    files = results.get('files', [])

    if files:
        return files[0]['id']

    folder_metadata = {
        'name': folder_name,
        'mimeType': 'application/vnd.google-apps.folder'
    }

    folder = service.files().create(body=folder_metadata, fields='id').execute()

    return folder.get('id')


def upload_file(file_path):

    service = authenticate_drive()

    folder_id = get_backup_folder(service)

    file_name = os.path.basename(file_path)

    query = f"name='{file_name}' and '{folder_id}' in parents"

    results = service.files().list(q=query, fields="files(id, name)").execute()

    existing_files = results.get('files', [])

    media = MediaFileUpload(file_path)

    if existing_files:

        file_id = existing_files[0]['id']

        service.files().update(
            fileId=file_id,
            media_body=media
        ).execute()

        print(f"{file_name} updated in Healthcare_Backups folder")

    else:

        file_metadata = {
            'name': file_name,
            'parents': [folder_id]
        }

        service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id'
        ).execute()

        print(f"Uploaded {file_name} to Healthcare_Backups folder")