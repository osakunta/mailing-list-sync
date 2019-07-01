from .api_connection import service


def insert(group_key, member):
    return service.members().insert(groupKey=group_key, body=member).execute()


def list_all(group_key, page_token=None):
    response = service.members().list(groupKey=group_key, pageToken=page_token).execute()
    members = response.get('members')

    try:
        return members + list_all(group_key, page_token=response['nextPageToken'])
    except KeyError:
        return members
