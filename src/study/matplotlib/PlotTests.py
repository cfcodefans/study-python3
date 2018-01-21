import unittest
from datetime import datetime
from io import StringIO
from typing import Iterable

import matplotlib.animation as anim
import matplotlib.dates as mdates
import matplotlib.lines as Lines
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.pyplot import *
from pandas import DataFrame, Series

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

    def test_coordinates(self):
        fig: Figure = plt.figure(figsize=(8, 3))
        print(fig)
        print(fig.axes)
        ax1: Axes = fig.add_axes((0.1, 0.1, 0.3, 0.8))
        ax1.set_facecolor('w')
        ax2: Axes = fig.add_axes((0.6, 0.1, 0.3, 0.8))
        ax2.set_facecolor('w')
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

    def test_simple(self):
        _x: np.ndarray = np.arange(1, 10, 1)
        _y: np.ndarray = _x * 0.75
        df: DataFrame = DataFrame()
        df['x'] = _x.tolist()
        df['y'] = _y.tolist()
        df
        fig: Figure = plt.figure(figsize=(8, 6))
        print(fig)
        ax: Axes = fig.add_axes([1, 1, 6, 4])

        ax.set_xticks(df['x'])
        ax.set_yticks(df['y'])
        ax.set_xlabel('x')
        ax.set_ylabel('y')

        plt.plot(df['x'], df['y'])
        print(ax)
        plt.show()

    def test_df(self) -> DataFrame:
        raw_str: str = '''
DATA,H,L,C,TR,N
20021102,0.7220,0.7124,0.7124,0.0096,0.0134
20021104,0.7170,0.7073,0.7073,0.0097,0.0132
20021105,0.7099,0.6723,0.6723,0.0176,0.0134
20021106,0.6930,0.6800,0.6838,0.0130,0.0134
20021107,0.6960,0.6736,0.6736,0.0224,0.0139
20021108,0.6820,0.6706,0.6706,0.0114,0.0137
20021111,0.6820,0.6710,0.6710,0.0114,0.0136
20021112,0.6795,0.6720,0.6744,0.0085,0.0134
20021113,0.6760,0.6550,0.6616,0.0210,0.0138
20021114,0.6650,0.6585,0.6627,0.0065,0.0134
20021115,0.6701,0.6620,0.6701,0.0081,0.0131
20021118,0.6965,0.6750,0.6965,0.0264,0.0138
20021119,0.7065,0.6944,0.6944,0.0121,0.0137
20021120,0.7115,0.6944,0.7087,0.0171,0.0139
20021121,0.7168,0.7100,0.7124,0.0081,0.0136
20021122,0.7265,0.7120,0.7265,0.0145,0.0136
20021125,0.7265,0.7098,0.7098,0.0167,0.0138
20021126,0.7184,0.7110,0.7184,0.0086,0.0135
20021127,0.7280,0.7200,0.7228,0.0096,0.0133
20021202,0.7375,0.7227,0.7359,0.0148,0.0134
20021203,0.7447,0.7310,0.7389,0.0137,0.0134
20021204,0.7420,0.7140,0.7162,0.0280,0.0141
20021205,0.7340,0.7207,0.7284,0.0178,0.0143
        '''

        df: DataFrame = pd.read_csv(StringIO(raw_str), delimiter=',')
        # print(df.keys())
        df['DATA'] = df['DATA'].apply(lambda d: datetime.strptime(str(d), '%Y%m%d').date())
        return df

    def test_two_axes(self):
        df: DataFrame = self.test_df()
        hs: Series = df['H']
        # print(hs)
        d_size: int = len(df)

        date_fmt = mdates.DateFormatter('%Y-%m-%d')

        fig: Figure = plt.figure(figsize=(11, 5))

        ax_h: Axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        ax_h.set_xticks(range(0, d_size), 1)
        ax_h.xaxis.set_major_formatter(date_fmt)
        ax_h.xaxis.set_major_locator(mdates.AutoDateLocator())

        # ax_h.twinx().plot(df['DATA'], df['C'], color='y')
        ax_h.plot(df['DATA'], df['H'], color='r')
        ax_h.plot(df['DATA'], df['C'], color='g')
        ax_h.plot(df['DATA'], df['L'], color='b')

        ax_2: Axes = ax_h.twinx()
        ax_2.plot(df['DATA'], df['TR'], color='k')
        ax_2.plot(df['DATA'], df['N'], color='m')

        plt.show()


if __name__ == '__main__':
    unittest.main()
