from dotenv import load_dotenv
import os

load_dotenv()

ENV = os.environ.get('ENV')
SERVICE_ACCOUNT_FILE = os.environ.get('SERVICE_ACCOUNT_FILE')
DELEGATED_USER = os.environ.get('DELEGATED_USER')

SCOPES = [
    'https://www.googleapis.com/auth/admin.directory.group',
    'https://www.googleapis.com/auth/spreadsheets.readonly'
]
