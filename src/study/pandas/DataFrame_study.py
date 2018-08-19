import unittest as ut
from typing import List
import pandas as pd
from pandas import *
from io import StringIO

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


class DataFrameTests(ut.TestCase):
    df: DataFrame = pd.read_csv(StringIO(raw_str), delimiter=',')

    def test_df_keys(self):
        keys: Index = self.df.keys()
        print(f'keys: {keys}')
        print(f'keys len: {len(keys)}')
        print(f'keys[1]: {keys[1]}')
        print(f'keys[-1]: {keys[-1]}')
        # print(f'keys[1]: {keys["H"]}')

    def test_df_RangeIndex(self):
        print(f'axes {self.df.axes}', self.df.axes.__class__)
        rowIdx: RangeIndex = self.df.axes[0]
        print(rowIdx)
        print(rowIdx[1], rowIdx[-1], rowIdx[1:-1])
        print([i for i in rowIdx])

    def test_df_oper(self):
        _df: DataFrame = DataFrame(self.df['H'] - self.df['L'], columns=['DIFF'])
        print(_df.keys())
        print(_df.axes)
        print(_df)
        # print(pd.concat([self.df['H'], self.df['L']]))
        h_ls: DataFrame = self.df[['H', 'L']]
        h_ls['DIFF'] = _df['DIFF']
        print(h_ls)

    def test_df_plot(self):
        import matplotlib.pyplot as plt
        plt.show()

    pass


if __name__ == '__main__':
    ut.main()
