# impoting stock prices


import pandas as pd
import pandas_datareader as web
import numpy as np
import matplotlib.pyplot as plt


stock = web.get_data_yahoo("AAPL", start = "2017-01-01", end = "2018-03-01")

price = stock["Adj Close"]

d_returns = price.pct_change()

print(d_returns)
plt.plot(d_returns)
plt.show()






