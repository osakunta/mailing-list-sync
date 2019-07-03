from googleapiclient.discovery import build
from google.oauth2 import service_account
from src.config import GOOGLE_API, ENV


def __create_api_connection():
    if ENV == 'test':
        return

    credentials = service_account.Credentials.from_service_account_file(
        GOOGLE_API['service_account_file'], scopes=GOOGLE_API['sheets_scopes']
    )

    return build('sheets', 'v4', credentials=credentials, cache_discovery=False)


service = __create_api_connection()
