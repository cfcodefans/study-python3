import unittest
from unittest import *

from __builtin__ import xrange


class RangeTests(TestCase):
    def test_range(self):
        print(range(1, 10))
        print(xrange(start=1, stop=10, step=2))


if __name__ == "main":
    unittest.main()
