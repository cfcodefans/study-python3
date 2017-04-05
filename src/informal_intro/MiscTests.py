import unittest
from functools import reduce
from itertools import chain


class MiscTests(unittest.TestCase):
    def test_repeat(self):
        print([1] * 2)

    def test_chain(self):
        print(list(chain([[1] * 2, [2] * 2])))

    def test_reduce(self):
        print(reduce(lambda a, b: a + b, [[1] * 2, [2] * 2]))


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
