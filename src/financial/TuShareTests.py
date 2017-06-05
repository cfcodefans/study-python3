import tushare
import unittest
import os


class TuShareTests(unittest.TestCase):
    # def test_version(self):
    #     print(tushare.__version__)

    def test_000290(self):
        print(tushare.get_fund_info("000290"))
        history = tushare.get_nav_history("000290", start="2015-01-01")
        print(history)

        data_path = "S:/data/funds/000290"
        if not os.path.exists(data_path):
            os.makedirs(data_path)
        data_file = data_path + "/history.csv"
        if os.path.exists(data_file):
            os.remove(data_file)
        history.to_csv(data_file)

    pass


if __name__ == '__main__':
    unittest.main()
