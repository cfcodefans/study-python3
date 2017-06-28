import matplotlib.pyplot as plt
import numpy as np
import logging
from typing import *
import unittest
# import tensorflow as tf

logging.basicConfig(format="%(asctime)s\t%(levelname)s\t%(message)s", level=logging.INFO)


def soft_max(x: List[float]) -> np.ndarray:
    """Compute softmax values for x"""
    # pass  # TODO: Compute and return softmax(x)
    _sum: float = sum([np.exp(_x) for _x in x])
    return np.array([np.exp(_x) / _sum for _x in x])


def main():
    print(soft_max([0.3, 0.1, 0.2]))
    # Plot softmax curves
    x: np.ndarray = np.arange(start=-2.0, stop=6.0, step=0.1)
    print("x:\n", x)
    scores = np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])
    print("scores:\n", scores)
    plt.plot(x, soft_max(scores).T, linewidth=2)
    plt.show()


class SoftMaxTests(unittest.TestCase):
    @unittest.skip
    def test_np_exp(self):
        import math
        for i in range(1, 10):
            print(i, np.exp(i), math.e ** i)

        x: np.ndarray = np.arange(start=0.1, stop=1, step=0.1)
        plt.plot(x, np.exp(x))
        plt.show()

    def test_numerical_unstability(self):
        f = 1000000000 + 0.000001 - 1000000000
        print("{:f}".format(f))

    @unittest.skip
    def test_soft_max(self):
        print(soft_max(np.arange(1, 4)))
        print(soft_max(np.arange(10, 40, 10)))
        print(soft_max(np.arange(0.1, 0.4, 0.1)))


if __name__ == '__main__':
    # main()
    unittest.main()
