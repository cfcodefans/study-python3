import unittest


class CalculatorTests(unittest.TestCase):
    def test_math(self):
        self.assertEqual(2 + 2, 4, "2 + 2 = 4")
        self.assertEqual(50 - 5 * 6, 20, "50 - 5 * 6 = 20")
        self.assertEqual((50 - 5 * 6) / 4, 5, "(50 - 5 * 6) / 4 = 5")
        self.assertEqual(8 / 5, 1.6, "8 / 5 = 1.6")
        self.assertAlmostEqual(17 / 3, 5.66, 1, "17 / 3 = 5.66")
        self.assertEqual(17 // 3, 5, "17 // 3 = 5")
        self.assertEqual(17 % 3, 2, "17 % 3 = 2")
        self.assertEqual(17 % -3, -1, "17 % -3 = -1")
        self.assertEqual(-17 % 3, 1, "-17 % 3 = 1")
        self.assertEqual(-17 % -3, -2, "-17 % -3 = -2")


if __name__ == '__main__':
    unittest.main()
