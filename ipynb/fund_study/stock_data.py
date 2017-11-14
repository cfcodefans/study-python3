import tushare as ts
import unittest as ut
import pandas as pd


class TuShareTests(ut.TestCase):
    print(ts.__version__, "\n")

    def test_stock_1(self):
        s_sh: pd.DataFrame = ts.get_k_data(code="sh", start="2017-01-01", ktype="D")
        print(s_sh)

    def test_boxoffice_1(self):
        bf: pd.DataFrame = ts.realtime_boxoffice()
        print(bf)
        bf: pd.DataFrame = ts.day_boxoffice()
        print(bf)

    pass


if __name__ == '__main__':
    ut.main()
