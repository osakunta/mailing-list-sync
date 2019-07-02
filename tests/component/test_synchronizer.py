import unittest
from src.google.directory import members


def list_all_mock(arg):
    return []


def insert_and_remove_in_batch_mock(*args):
    return True


members.list_all = list_all_mock
members.insert_and_remove_in_batch = insert_and_remove_in_batch_mock


class TestSynchronizer(unittest.TestCase):

    def test_synchronizer(self):
        self.assertEqual(members.list_all(''), [])
        self.assertTrue(members.insert_and_remove_in_batch('', [], []))


if __name__ == '__main__':
    unittest.main()
