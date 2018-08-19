import unittest


class Polynomial:
    def __init__(self, *coeffs: float):
        self.coeffs = coeffs

    def __repr__(self):
        return f'Polynomial({self.coeffs})'

    def __add__(self, other):
        return Polynomial(*(x + y for x, y in zip(self.coeffs, other.coeffs)))

    def __len__(self):
        return len(self.coeffs)

    # def __index__(self, idx: int):
    #     return self.coeffs[idx]


class PolynomialTests(unittest.TestCase):

    def testInit(self):
        p1: Polynomial = Polynomial(1, 2, 3)
        p2: Polynomial = Polynomial(4, 5, 6)

        print(p1)
        print(p2)

    def testLen(self):
        p1: Polynomial = Polynomial(1, 2, 3)
        print(p1)
        print(len(p1))

    def testAdd(self):
        print(Polynomial(1, 2, 3) + Polynomial(4, 5, 6))

    def testIndex(self):
        p1: Polynomial = Polynomial(1, 2, 3)
        print(p1[2])
