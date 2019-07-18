from googleapiclient.discovery import build
from google.auth import default
from src.config import GOOGLE_API, ENV


def connect_to_api(api_name, api_version, scopes=None, delegation=False):
    if ENV == 'test':
        return

    credentials, _ = default(scopes=scopes)

    if delegation:
        credentials = credentials.with_subject(GOOGLE_API['delegated_user'])

    return build(api_name, api_version, credentials=credentials, cache_discovery=False)
