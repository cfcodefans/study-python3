import unittest

class CalculatorTests (unittest.TestCase):
    def test_math(self):
        self.assertEqual(2 + 2, 4, "2 + 2 = 4")

if __name__ == '__main__':
    unittest.main()