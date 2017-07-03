import unittest


class ListTests(unittest.TestCase):
    def test_delete(self):
        _list:list = list(range(3, 9))
        print(_list)
        _list.remove(5)
        print(_list)

    def test_sort(self):
        _list: list = list(range(9, 3, -1))
        print(_list)
        _list.sort()
        print(_list)

if __name__ == '__main__':
    unittest.main