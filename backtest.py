# impoting stock prices


import pandas as pd
import pandas_datareader as web
import numpy as np
import matplotlib.pyplot as plt


stock = web.get_data_yahoo("AAPL", start = "2017-01-01", end = "2018-03-01")

price = stock["Adj Close"]

d_returns = price.pct_change()

print(d_returns)
#plt.plot(d_returns)
#plt.show()

d_returns = d_returns.to_frame()


# preparation for prophet intake
d_returns["ds"] = d_returns.index # create ds column from index
d_returns["y"] = d_returns["Adj Close"] # create y column from adj close price

d_returns.drop('Adj Close', axis=1, inplace=True) # drop original adj close price column


d_returns = d_returns.reset_index(drop=True)


d_returns = d_returns.set_index('ds')


print(d_returns)







