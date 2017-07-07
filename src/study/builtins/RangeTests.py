import unittest


class RangeTests(unittest.TestCase):
    def test_create_range(self):
        r: range = range(50, 100)
        print(r.count(200))


if __name__ == '__main__':
    unittest.main
