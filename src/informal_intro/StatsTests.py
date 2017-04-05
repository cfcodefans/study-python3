from functools import reduce
from math import *

from typing import List, Dict
from itertools import groupby, chain


def mean_median_mode():
    # n: int = int(input())
    # array: List[int] = [int(s) for s in input().split(" ")]
    array = [3, 1, 4, 1, 5]
    _sum: int = sum(array)
    print("{0:.1f}".format(_sum / len(array)))

    _len: int = len(array)
    half: int = int(_len / 2)
    _sorted: List[int] = sorted(array)
    median: float = _sorted[half]
    if _len % 2 == 0:
        median = (_sorted[half - 1] + median) / 2
    print("{0:.1f}".format(median))

    d: Dict[int, int] = dict([(k, 0) for k in array])
    for e in array:
        d[e] += 1

    _d: Dict[int, List[int]] = dict([(c, []) for c in d.values()])
    for k, c in d.items():
        _d[c].append(k)

    print(min(_d[max(_d.keys())]))


def weighted_mean():
    n = int(input())
    X = [int(s) for s in input().split(" ")]
    W = [int(s) for s in input().split(" ")]
    print("{0:.1f}".format(sum([x * w for x, w in zip(X, W)]) / sum(W)))


def quartiles():
    def median_sorted(_sorted):
        _len = len(_sorted)
        if _len == 0:
            return None
        mid = int(_len / 2)
        return (_sorted[mid] + _sorted[mid - 1 + _len % 2]) / 2

    n = 9  # int(input())
    array = [int(s) for s in "3 7 8 5 12 14 21 13 18".split(" ")]
    _sorted = sorted(array)
    print("{0:.0f}".format(median_sorted(_sorted[0: int(n / 2)])))
    print("{0:.0f}".format(median_sorted(_sorted)))
    print("{0:.0f}".format(median_sorted(_sorted[int(n / 2) + n % 2: n])))


def interquartile_range():
    def median_sorted(_sorted):
        _len = len(_sorted)
        if _len == 0:
            return None
        mid = int(_len / 2)
        return (_sorted[mid] + _sorted[mid - 1 + _len % 2]) / 2

    n = int(input())
    X = [int(x) for x in input().split(" ")]
    F = [int(f) for f in input().split(" ")]
    S = sorted(reduce(lambda a, b: a + b, [[x] * f for x, f in zip(X, F)]))
    _len = len(S)
    print("{0:.0f}".format(median_sorted(S[int(_len / 2) + _len % 2: _len]) - median_sorted(S[0: int(_len / 2)])))


def standard_deviation():
    n = int(input())
    X = [int(x) for x in input().split(" ")]
    mean = sum(X) / n
    print("{0:.1f}".format(sqrt(sum([(x - mean) ** 2 for x in X]) / n)))


if __name__ == '__main__':
    standard_deviation()
