from unittest import *
import unittest as ut


class LangTests(TestCase):

    def test_or(self):
        print(None or "abc")
        print(None or 1)
        print(123 or "abc")
        print(123 or None or "abc")


if __name__ == '__main__':
    ut.main()
