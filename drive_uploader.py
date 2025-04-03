from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import os
import config
from google.oauth2.service_account import Credentials

def authenticate_google_drive():
    creds = Credentials.from_service_account_file(config.SERVICE_ACCOUNT_FILE, scopes=[
        "https://www.googleapis.com/auth/drive"
    ])
    return build("drive", "v3", credentials=creds)

def upload_to_google_drive(local_folder):
    service = authenticate_google_drive()
    
    for filename in os.listdir(local_folder):
        filepath = os.path.join(local_folder, filename)
        file_metadata = {"name": filename, "parents": [config.GOOGLE_DRIVE_FOLDER_ID]}
        media = MediaFileUpload(filepath, mimetype="image/jpeg")

        service.files().create(body=file_metadata, media_body=media, fields="id").execute()
