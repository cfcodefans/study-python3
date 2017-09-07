import os
import csv
from typing import Iterable, List, Tuple
import random

import math

Row = List[float]
Rows = List[Row]

path: str = os.path.dirname(__file__)
print(path)
data_path = path + "/pima-indians-diabetes.data"


def loadCsv(file_path: str) -> Rows:
    rows: Iterable = csv.reader(open(data_path))
    return [[float(x) for x in row] for row in rows]


data: Rows = loadCsv(data_path)
print(f"loaded {len(data)} lines")


def split_data(_data: Rows, ratio: float) -> (Rows, Rows):
    split_size: int = int(len(_data) * ratio)
    copy: Rows = _data.copy()
    train_data: Rows = []
    while len(train_data) < split_size:
        index: int = random.randrange(len(copy))
        train_data.append(copy.pop(index))

    return train_data, copy


train: Rows
test: Rows
train, test = split_data(data, 0.67)

print(f"train has {len(train)},\ttest has {len(test)}")


def separate_by_class(_data: Rows) -> {int, Rows}:
    class_1: Rows = [row for row in _data if row[-1] == 1]
    class_0: Rows = [row for row in _data if row[-1] == 0]
    return {1: class_1, 0: class_0}


def mean(nums: List[float]) -> float:
    return sum(nums) / float(len(nums))


def stdev(nums: List[float], _mean: float = math.nan) -> float:
    avg: float = _mean
    if avg == math.nan:
        avg = mean(nums)
    variance: float = sum([(x - avg) ** 2 for x in nums]) / float(len(nums) - 1)
    return math.sqrt(variance)


def mean_stdev(nums: List[float]) -> (float, float):
    avg: float = mean(nums)
    return avg, stdev(nums, avg)


def summarize(_data: Rows) -> (float, float):
    summaries: List[(float, float)] = [mean_stdev(attribute) for attribute in zip(*_data)]
    del summaries[-1]
    return summaries


MeanAndStdDev = Tuple[float, float]


def summarize_by_class(_data: Rows) -> {int: List[MeanAndStdDev]}:
    by_class: {int, Rows} = separate_by_class(_data)
    return dict([(class_val, summarize(instance)) for class_val, instance in by_class.items()])


Summary = {int: List[MeanAndStdDev]}
summary: Summary = summarize_by_class(data)
[print(k, v) for k, v in summary.items()]


def calculate_gaussian_probability(x: float, avg: float, dev: float) -> float:
    exponent: float = math.exp(-((x - avg) ** 2) / (2 * dev ** 2))
    return (1 / (math.sqrt(2 * math.pi) * dev)) * exponent


def calculate_class_probability(_summary: Summary, sample: Row) -> {int, float}:
    probability: {int, float} = {}
    for class_value, class_summary in _summary.items():
        probability[class_value] = 1
        for i in range(len(class_summary)):
            _mean: float
            _stdev: float
            _mean, _stdev = class_summary[i]
            x = sample[i]
            probability[class_value] *= calculate_gaussian_probability(x, _mean, _stdev)

    return probability


correct_count: int = 0
for sample in test:
    result: {int, float} = calculate_class_probability(summary, sample)
    print(sample[-1], result[1] > result[0], "\t0 %.20f" % result[0], "1 %.20f" % result[1])
    if sample[-1] == 1 and result[1] > result[0]:
        correct_count += 1
    elif sample[-1] == 0 and result[1] < result[0]:
        correct_count += 1

print(len(test), correct_count)
