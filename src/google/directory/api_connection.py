from googleapiclient.discovery import build
from google.oauth2 import service_account
from src.google.api_config import ENV, SERVICE_ACCOUNT_FILE, DELEGATED_USER, SCOPES


def __create_api_connection():
    if ENV == 'test':
        return

    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )

    delegated_credentials = credentials.with_subject(DELEGATED_USER)

    return build('admin', 'directory_v1', credentials=delegated_credentials)


service = __create_api_connection()
