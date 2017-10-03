from datetime import date, datetime
import unittest as ut


class DateTimeTests(ut.TestCase):
    def test_format(self):
        d: date = datetime.now().date()
        print(d)
        print(d.strftime("%Y-%m-%d"))
        d = date(2017, 6, 1)
        print(d)
        print(d.strftime("%Y-%m-%d"))


if __name__ == '__main__':
    ut.main()
