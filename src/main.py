from __future__ import print_function
from googleapiclient.discovery import build
from google.oauth2 import service_account
from dotenv import load_dotenv
import os

load_dotenv()

SCOPES = ['https://www.googleapis.com/auth/admin.directory.group']
SERVICE_ACCOUNT_FILE = os.environ.get('SERVICE_ACCOUNT_FILE')
DELEGATED_USER = os.environ.get('DELEGATED_USER')


def create_api_connection():
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )

    delegated_credentials = credentials.with_subject(DELEGATED_USER)

    return build('admin', 'directory_v1', credentials=delegated_credentials)


def main():
    service = create_api_connection()

    print('Getting the first 10 groups in the domain')
    results = service.groups().list(customer='my_customer', maxResults=10).execute()

    groups = results.get('groups', [])

    if not groups:
        print('No groups in the domain.')
    else:
        print('Groups:')
        for group in groups:
            print(u'{0} ({1})'.format(group['name'], group['email']))


if __name__ == '__main__':
    main()
