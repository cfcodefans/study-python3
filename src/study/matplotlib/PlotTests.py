from typing import Iterable

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as Lines
import matplotlib.animation as anim
from matplotlib.artist import Artist
import unittest

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
    def test_try(self):
        fig1: plt.Figure = plt.figure()

        data: np.ndarray = np.random.rand(2, 25)

        [line] = plt.plot([], [], 'r-')
        print("line,:\t", str(line))

        plt.xlim(0, 1)
        plt.xlim(0, 1)
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
