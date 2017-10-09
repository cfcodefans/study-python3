import unittest
from typing import List


class LambdaTests(unittest.TestCase):
    def test_lambda(self):
        li: List = list(range(100))
        li.sort(key=lambda x: x % 10)
        print(li)

    pass


if __name__ == '__main__':
    unittest.main()
