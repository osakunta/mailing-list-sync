from dotenv import load_dotenv
import logging
import os

load_dotenv()

ENV = os.environ.get('ENV')

GOOGLE_API = {
    'service_account_file': os.environ.get('SERVICE_ACCOUNT_FILE'),
    'delegated_user': os.environ.get('DELEGATED_USER'),
    'directory_scopes': ['https://www.googleapis.com/auth/admin.directory.group'],
    'sheets_scopes': ['https://www.googleapis.com/auth/spreadsheets.readonly'],
}


def setup_logging():
    logging.getLogger('googleapiclient.discovery').setLevel(logging.ERROR)
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)
