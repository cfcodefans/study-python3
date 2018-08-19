from os import path
import unittest


class FileSystemTests(unittest.TestCase):

    def test_current_path(self):
        print(path.abspath(path.curdir))
        import math
        math.e
    pass

    def test_read_file(self):
        t = open("./FileSystemTests.py")
        print(t)


if __name__ == '__main__':
    unittest.main()