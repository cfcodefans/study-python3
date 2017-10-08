

from datetime import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from ipynb.fund_study.fund_data import get_fund_data

data: np.ndarray = get_fund_data("001878", sdate=date(2016, 10, 1))
print(len(data), data[0], type(data[0][0]))

xd: np.ndarray = np.array([_date[0] for _date in data[0:len(data), 0:1]])
value_yd: np.ndarray = np.array([data[i][2] for i in range(0, len(xd))])

years = mdates.YearLocator()   # every year
months = mdates.MonthLocator()  # every month
yearsFmt = mdates.DateFormatter('%Y')

# load a numpy record array from yahoo csv data with fields date,
# open, close, volume, adj_close from the mpl-data/example directory.
# The record array stores python datetime.date as an object array in
# the date column

fig, ax = plt.subplots()


# format the ticks
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(yearsFmt)
ax.xaxis.set_minor_locator(months)

# datemin = datetime.date(r.date.min().year, 1, 1)
# datemax = datetime.date(r.date.max().year + 1, 1, 1)
# ax.set_xlim(datemin, datemax)

# format the coords message box
def price(x):
    return '$%1.2f' % x
ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')
ax.format_ydata = price
ax.grid(True)

ax.plot(xd, value_yd)

# rotates and right aligns the x labels, and moves the bottom of the
# axes up to make room for them
fig.autofmt_xdate()

plt.show()