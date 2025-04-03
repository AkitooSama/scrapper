import gspread
from google.oauth2.service_account import Credentials
import config

def authenticate_google_sheets():
    creds = Credentials.from_service_account_file(config.SERVICE_ACCOUNT_FILE, scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ])
    return gspread.authorize(creds)

def get_hashtags():
    client = authenticate_google_sheets()
    sheet = client.open_by_key(config.SHEET_ID).worksheet(config.SHEET_NAME)
    return [row[0] for row in sheet.get_all_values() if row]
