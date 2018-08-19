# https://brilliant.org/practice/expected-value-in-quant-finance/?p=8
def solve_expected_value():
    def i_d(i: int) -> int:
        _bin: str = bin(i)
        d: int = 0
        for i in range(0, len(_bin) - 1):
            if _bin[i] == '1' and _bin[i + 1] == '1':
                d += 1
        return d

    d_c: dict[int, int] = {}
    for i in range(0, 2 ** 10):
        d: int = i_d(i)
        # print(i, bin(i), d)
        if not d in d_c:
            d_c[d] = 1
        else:
            d_c[d] = d_c[d] + 1

    print(d_c)
    expected: float = sum([d * c / 1024 for d, c in d_c.items()])
    print(expected)


solve_expected_value()
