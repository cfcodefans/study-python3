import numpy as np
import unittest as ut


class NumpyTests(ut.TestCase):
    def test_try_ndarray(self):
        arr: np.ndarray = np.array([list(range(1, x)) for x in range(1, 10)])
        print(arr)

    def test_col_ndarray(self):
        arr: np.ndarray = np.array([list(range(x * 10, x * 10 + 10)) for x in range(0, 10)])
        print(arr)
        print(arr[0:len(arr), 0:1])
        print(arr[0:len(arr), 4:6])
        print(arr[0:len(arr), 4:6])


if __name__ == '__main__':
    ut.main()
