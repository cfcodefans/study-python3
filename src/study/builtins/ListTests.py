import unittest


class ListTests(unittest.TestCase):
    def setUp(self):
        print()

    def test_repeat(self):
        print([1] * 5)


    def test_delete(self):
        _list: list = list(range(3, 9))
        print(_list)
        _list.remove(5)
        print(_list)

    def test_sort(self):
        _list: list = list(range(9, 3, -1))
        print(_list)
        _list.sort()
        print(_list)

    def test_index(self):
        _list: list = list(range(0, 10))
        print(_list)
        print(_list[5])
        print(_list[5:])
        print(_list[:5])
        print(_list[-3])
        print(_list[-3:])
        print(_list[:-3])

    def test_add(self):
        print([2] + [4])
        print([2].append(4))

if __name__ == '__main__':
    unittest.main
