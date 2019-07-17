from googleapiclient.discovery import build
from google.oauth2 import service_account
from google.auth import compute_engine
from src.config import GOOGLE_API, ENV


def connect_to_api(api_name, api_version, scopes=None, delegation=False):
    if ENV == 'test':
        return

    if ENV == 'development':
        credentials = service_account.Credentials.from_service_account_file(
            GOOGLE_API['service_account_file'], scopes=scopes
        )
    else:
        credentials = compute_engine.Credentials()

    if delegation:
        credentials = credentials.with_subject(GOOGLE_API['delegated_user'])

    return build(api_name, api_version, credentials=credentials, cache_discovery=False)
