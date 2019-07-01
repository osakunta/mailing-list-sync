from directory_api import members


def synchronize_group(group_key, new_list):
    old_list = __get_old_list(group_key)
    insert_items, remove_items = __get_diff(old_list, new_list)

    if not (insert_items or remove_items):
        print('Group {} is already synchronized'.format(group_key))
        return

    print('Synchronizing group: {}'.format(group_key))

    if insert_items:
        print('Adding following email addresses ({}) to the group:'.format(len(insert_items)))
        print(insert_items)

    if remove_items:
        print('Deleting following email addresses ({}) from the group:'.format(len(remove_items)))
        print(remove_items)

    members.insert_and_remove_in_batch(group_key, insert_items, remove_items)


def __get_old_list(group_key):
    old_group = members.list_all(group_key)
    old_list = []

    for member in old_group:
        old_list = old_list + [member['email']]

    return old_list


def __get_diff(old_list, new_list):
    old_set = set(old_list)
    new_set = set(new_list)

    insert_items = new_set - old_set
    remove_items = old_set - new_set

    return insert_items, remove_items
