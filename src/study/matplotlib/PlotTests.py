from typing import Iterable

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as Lines
import matplotlib.animation as anim
from matplotlib.artist import Artist
import unittest

from datetime import datetime
import matplotlib.dates as mdates

'''
func : callable
       The function to call at each frame.  The first argument will
       be the next value in ``frames``.   Any additional positional
       arguments can be supplied via the ``fargs`` parameter.
       The required signature is ::
          def func(fr: object, *fargs) -> iterable_of_artists:
'''


def update_line(num, data, line: Lines.Line2D) -> Iterable[Artist]:
    print("num:\t", num, "line:\t", line)
    line.set_data(data[...:num])
    return line,


class PlotTests(unittest.TestCase):
    def test_date_x(self):
        # 生成横纵坐标信息
        dates = ['01/02/1991', '01/03/1991', '01/04/1991']
        xs = [datetime.strptime(d, '%m/%d/%Y').date() for d in dates]
        [print(xd) for xd in xs]
        ys = [[i, i * 2] for i in range(0, 3)]
        # 配置横坐标
        xaxis = plt.gca().xaxis
        xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
        xaxis.set_major_locator(mdates.DayLocator())
        # Plot
        plt.plot(xs, ys)
        plt.gcf().autofmt_xdate()  # 自动旋转日期标记
        plt.show()

    def test_try(self):
        fig1: plt.Figure = plt.figure()

        data: np.ndarray = np.random.rand(2, 25)

        [line] = plt.plot([], [], 'r-')
        print("line,:\t", str(line))

        plt.xlim(0, 1)
        plt.ylim(0, 1)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('test')

        line_anim: anim.FuncAnimation = anim.FuncAnimation(fig1,
                                                           update_line,
                                                           25,
                                                           fargs=(data, line),
                                                           interval=50,
                                                           blit=False)  # can't work on windows

        plt.show()


if __name__ == '__main__':
    unittest.main()
