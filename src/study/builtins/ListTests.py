import unittest
from typing import List


class ListTests(unittest.TestCase):
    def setUp(self):
        print()

    def test_extend(self):
        print(["a"] + [2, 3, 4])

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
        # print(_list[...:5])

    def test_add(self):
        print([2] + [4])
        print([2].append(4))

    def test_get_index(self):
        print(list(range(10)).index(5))

    def test_unpack(self):
        a, = [0]
        print("a:\t", a)
        a, b = [1, 0]
        print("a:\t", a, "b:\t", b)

    def test_zip(self):
        _list: List[(float, float)] = [(1, 2), (2, 4), (3, 6)]
        _zip = zip(*_list)
        for x in _zip:
            print(x)

    def test_update(self):
        _list: List = [1, 2, 3]


if __name__ == '__main__':
    # unittest.main
    ListTests().test_zip()
