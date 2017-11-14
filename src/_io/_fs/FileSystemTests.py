from os import path
import unittest


class FileSystemTests(unittest.TestCase):

    def test_current_path(self):
        print(path.abspath(path.curdir))
        import math
        math.e
    pass


if __name__ == '__main__':
    unittest.main()