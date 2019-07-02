from src.googleintegration.directory.api_connection import service


def list_all(page_token=None):
    response = service.groups().list(customer='my_customer', pageToken=page_token).execute()
    groups = response.get('groups', [])

    try:
        return groups + list_all(page_token=response['nextPageToken'])
    except KeyError:
        return groups
