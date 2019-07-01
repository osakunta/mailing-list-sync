from googleapiclient.discovery import build
from google.oauth2 import service_account
from dotenv import load_dotenv
import os

load_dotenv()

SCOPES = ['https://www.googleapis.com/auth/admin.directory.group']
SERVICE_ACCOUNT_FILE = os.environ.get('SERVICE_ACCOUNT_FILE')
DELEGATED_USER = os.environ.get('DELEGATED_USER')


def __create_api_connection():
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )

    delegated_credentials = credentials.with_subject(DELEGATED_USER)

    return build('admin', 'directory_v1', credentials=delegated_credentials)


service = __create_api_connection()
