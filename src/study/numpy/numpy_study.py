import numpy as np
import unittest as ut


class NumpyTests(ut.TestCase):
    def test_try_ndarray(self):
        arr: np.ndarray = np.array([list(range(1, x)) for x in range(1, 10)])
        print(arr)

        arr_mix: np.ndarray = np.array(["a", 1, 0.5])
        print(arr_mix)

        arr = np.array([list(range(1, 10)) for x in range(1, 10)])
        arr_changed: np.ndarray = np.array([np.array(str(row[0])) + row[1:] for row in arr])
        print(arr)

    def test_col_ndarray(self):
        arr: np.ndarray = np.array([list(range(x * 10, x * 10 + 10)) for x in range(0, 10)])
        print(arr)
        print(arr[0:len(arr), 0:1])
        print(arr[0:len(arr), 4:6])
        print(arr[0:len(arr), 4:6])

    def test_filter(self):
        arr: np.ndarray = np.random.randn(100) * 100
        print(arr)

        positives: np.ndarray = arr[np.array([v > 0 for v in arr])]
        print(positives)

    def test_concate(self):
        arr1: np.ndarray = np.array(range(1, 5))
        arr2: np.ndarray = np.array(range(5, 10))
        print(arr1, arr2, np.append(arr1, arr2))


if __name__ == '__main__':
    ut.main()
