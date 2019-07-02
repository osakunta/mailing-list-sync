from dotenv import load_dotenv
import logging
import os

load_dotenv()
logging.getLogger('googleapiclient.discovery').setLevel(logging.ERROR)
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

ENV = os.environ.get('ENV')

GOOGLE_API = {
    'service_account_file': os.environ.get('SERVICE_ACCOUNT_FILE'),
    'delegated_user': os.environ.get('DELEGATED_USER'),
    'scopes': [
        'https://www.googleapis.com/auth/admin.directory.group',
        'https://www.googleapis.com/auth/spreadsheets.readonly'
    ]
}
