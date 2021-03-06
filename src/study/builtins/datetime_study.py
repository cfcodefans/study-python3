from datetime import date, datetime
import unittest as ut

from dateutil.parser import *


class DateTimeTests(ut.TestCase):
    def test_format(self):
        d: date = datetime.now().date()
        print(d)
        print(d.strftime("%Y-%m-%d"))
        d = date(2017, 6, 1)
        print(d)
        print(d.strftime("%Y-%m-%d"))

    def test_cmp(self):
        d: date = datetime.now().date()
        print(d)
        dp: date = date(2014, 1, 1)
        print(d < dp)

    def test_parser(self):
        d: date = datetime.now().date()
        print(parse(d.strftime("%Y-%m-%d")))


if __name__ == '__main__':
    ut.main()
