import logging
from src.google.directory.api_connection import service


def get():
    logging.info('Getting the first 10 groups in the domain')
    results = service.groups().list(customer='my_customer', maxResults=10).execute()

    groups = results.get('groups', [])

    if not groups:
        logging.info('No groups in the domain.')
    else:
        logging.info('Groups:')
        for group in groups:
            logging.info(u'{0} ({1})'.format(group['name'], group['email']))
