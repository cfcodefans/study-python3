import unittest


class RangeTests(unittest.TestCase):
    def test_create_range(self):
        r: range = range(50, 100)
        print(r.count(200))

    def test_range_tail(self):
        print(list(range(10)))


if __name__ == '__main__':
    unittest.main
