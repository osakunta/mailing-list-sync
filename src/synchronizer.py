from src.logger import log
from src.googleintegration.directory import members


def synchronize_group(group_key, new_list):
    old_list = __get_old_list(group_key)
    insert_items, remove_items = __get_diff(old_list, new_list)

    if not (insert_items or remove_items):
        log.info('Group {} is already synchronized'.format(group_key))
        return

    log.info('Synchronizing group: {}'.format(group_key))

    if insert_items:
        log.info('Adding following email addresses ({}) to the group:'.format(len(insert_items)))
        log.info(insert_items)

    if remove_items:
        log.info('Deleting following email addresses ({}) from the group:'.format(len(remove_items)))
        log.info(remove_items)

    members.insert_and_remove_in_batch(group_key, insert_items, remove_items)


def __get_old_list(group_key):
    old_group = members.list_all(group_key)
    old_list = map(lambda member: member['email'], old_group)

    return old_list


def __get_diff(old_list, new_list):
    old_set = set(old_list)
    new_set = set(new_list)

    insert_items = new_set - old_set
    remove_items = old_set - new_set

    return insert_items, remove_items
