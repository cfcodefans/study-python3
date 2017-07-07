import unittest
import random

class RandTests(unittest.TestCase):
    def test_randint(self):
        print(random.randint(0, 100))


if __name__ == '__main__':
    unittest.main
