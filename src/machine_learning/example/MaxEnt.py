# https://vimsky.com/article/776.html

import sys
import math
from collections import defaultdict


class MaxEnt:
    samples: list[tuple[str]] = []  # 样本集, 元素是[y,x1,x2,...,xn]的元组
    _Y: set[list[str]] = set([])  # 标签集合,相当于去重之后的y
    xy_counts: dict[(str, str), int] = defaultdict(int)  # Key是(xi,yi)对，Value是count(xi,yi)
    sample_num: int = 0  # count of samples
    num_distinct_samples: int = 0  # count of (xi, yi)
    _xyID: dict[(str, str), int] = {}  # 对(x,y)对做的顺序编号(ID), Key是(xi,yi)对,Value是ID
    _max_sample_vector_len: int = 0  # 样本最大的特征数量,用于求参数时的迭代，见IIS原理说明
    sample_expectation: list = []  # 样本分布的特征期望值
    model_expectation: list = []  # 模型分布的特征期望值
    weight_vector: list[float] = []  # 对应n个特征的权值
    last_weight_vector: list[float] = []  # 上一轮迭代的权值
    _EPS: float = 0.01  # 判断是否收敛的阈值

    def __init__(self):
        pass

    def load_data(self, filename: str):
        for line in open(filename, "r"):
            sample: list[str] = line.strip().split("\t")
            if len(sample) < 2:  # 至少：标签+一个特征
                continue
            y: str = sample[0]
            x: list[str] = sample[1:]
            self.samples.append(sample)  # labe + features
            self._Y.add(y)  # label
            for x in set(x):
                self.xy_counts[(x, y)] += 1

    def _init_params(self):
        self.sample_num = len(self.samples)
        self.num_distinct_samples = len(self.xy_counts)
        self._max_sample_vector_len = max([len(sample) - 1 for sample in self.samples])
        self.weight_vector = [0.0] * self.num_distinct_samples
        self.last_weight_vector = self.weight_vector[:]
        self.sample_ep()

    def sample_ep(self):
        self.sample_expectation = [0.0] * self.num_distinct_samples
        for i, xy in enumerate(self.xy_counts):
            self.sample_expectation[i] = self.xy_counts[xy] * 1.0 / self.sample_num
            self._xyID[xy] = i

    def _zx(self, xv: list[str]):
        ZX: float = 0.0
        for y in self._Y:
            _sum: float = 0.0
            for x in xv:
                if (x, y) in self.xy_counts:
                    _sum += self.weight_vector[self._xyID[(x, y)]]
            ZX += math.exp(_sum)
        return ZX

    def _pyx(self, X: list[str]):
        ZX: float = self._zx(X)
        results: list[(str, float)] = []
        for y in self._Y:
            _sum: float = 0.0
            for x in X:
                if (x, y) in self.xy_counts:
                    pass

        pass

    def _model_ep(self):
        self.model_expectation = [0.0] * self.num_distinct_samples
        for sample in self.samples:
            X: list[str] = sample[1:]
            pyx: list[(str, float)] = self._pyx(X)

    def train(self, max_iter: int = 1000):
        self._init_params()
        for i in range(0, max_iter):
            print(f"iterate:\t ${i}")
            self.last_weight_vector = self.weight_vector
            self._model_ep()
