import logging
from src.google.directory.api_connection import service


def list_all(group_key, page_token=None):
    response = service.members().list(groupKey=group_key, pageToken=page_token).execute()
    members = response.get('members', [])

    try:
        return members + list_all(group_key, page_token=response['nextPageToken'])
    except KeyError:
        return members


def insert_and_remove_in_batch(group_key, insert_list, remove_list):
    batch = service.new_batch_http_request()

    for email in insert_list:
        batch.add(__insert(group_key, {'email': email}), callback=__check_for_errors)

    for email in remove_list:
        batch.add(__delete(group_key, email), callback=__check_for_errors)

    return batch.execute()


def __insert(group_key, member):
    return service.members().insert(groupKey=group_key, body=member)


def __delete(group_key, member_key):
    return service.members().delete(groupKey=group_key, memberKey=member_key)


def __check_for_errors(request_id, response, exception):
    if exception is not None:
        logging.error(exception)
