from dotenv import load_dotenv
import logging
import os

load_dotenv()

ENV = os.environ.get('ENV', 'development')

GOOGLE_API = {
    'service_account_file': os.environ.get('SERVICE_ACCOUNT_FILE', None),
    'delegated_user': os.environ.get('DELEGATED_USER', None),
    'token_uri': 'https://accounts.google.com/o/oauth2/token',
    'directory_scopes': ['https://www.googleapis.com/auth/admin.directory.group'],
    'sheets_scopes': ['https://www.googleapis.com/auth/spreadsheets.readonly'],
}


def setup_logging():
    logging.getLogger('googleapiclient.discovery').setLevel(logging.ERROR)
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)
