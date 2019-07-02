from googleapiclient.discovery import build
from google.oauth2 import service_account
from src.config import GOOGLE_API, ENV


def __create_api_connection():
    if ENV == 'test':
        return

    credentials = service_account.Credentials.from_service_account_file(
        GOOGLE_API['service_account_file'], scopes=GOOGLE_API['scopes']
    )

    delegated_credentials = credentials.with_subject(GOOGLE_API['delegated_user'])

    return build('sheets', 'v4', credentials=delegated_credentials)


service = __create_api_connection()
