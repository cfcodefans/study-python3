import math


def poisson(mean: float, x: int) -> float:
    return (math.e ** -mean) * (mean ** x) / math.factorial(x)


print(poisson(5, 0))
print(poisson(5, 1))
print(poisson(5, 2))

print(poisson(4, 0))
print(poisson(8, 1))

print(poisson(3, 2))
print(poisson(3, 0) + poisson(3, 1))
print(1 - (poisson(3, 0) + poisson(3, 1) + poisson(3, 2)))

print(poisson(3.25, 3))
print(poisson(3.25, 0) + poisson(3.25, 1) + poisson(3.25, 2))
print(1 - (poisson(3.25, 0) + poisson(3.25, 1)))

print(sum([poisson(2.4, x) for x in range(4)]))
print(1 - sum([poisson(2.4, x) for x in range(2)]))
print(poisson(2.4, 3))
print(poisson(2, 0))
print(poisson(2, 2))
print(sum([poisson(4, x) for x in range(3)]))
print(poisson(2.5, 0))
print(1 - sum([poisson(15 / 4, x) for x in range(4)]))
