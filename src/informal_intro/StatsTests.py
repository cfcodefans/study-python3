from functools import reduce

from typing import List, Dict
from itertools import groupby


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


if __name__ == '__main__':
    weighted_mean()
