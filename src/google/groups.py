from .api_connection import service


def get():
    print('Getting the first 10 groups in the domain')
    results = service.groups().list(customer='my_customer', maxResults=10).execute()

    groups = results.get('groups', [])

    if not groups:
        print('No groups in the domain.')
    else:
        print('Groups:')
        for group in groups:
            print(u'{0} ({1})'.format(group['name'], group['email']))
