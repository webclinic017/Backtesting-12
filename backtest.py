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


ratio = 0.90
row_len = d_returns.shape[0]
cut_off = round(ratio * row_len)
period_forecast = row_len - cut_off 



train = d_returns['y'][0:cut_off]
train = train.to_frame()
train.insert(0, 'ds', train.index)
train = train.reset_index(drop=True)

print(train)







from fbprophet import Prophet
# prophet preformance
from fbprophet.diagnostics import cross_validation
from fbprophet.diagnostics import performance_metrics
from fbprophet.plot import plot_cross_validation_metric


# set prophet model 
prophet = Prophet(changepoint_prior_scale=0.15, daily_seasonality=False)



prophet.fit(train)


build_forecast = prophet.make_future_dataframe(periods=period_forecast, freq='D')

forecast = prophet.predict(build_forecast)


# plot forecasts
#prophet.plot(forecast, xlabel='Date', ylabel='retrun')
#plt.title('Predicted stock returns')
# display graph
#plt.show()


# tell us more about the forecast
#prophet.plot_components(forecast)



print(forecast.iloc[-period_forecast:-1].yhat)
prediction = pd.DataFrame()
prediction['y'] = (forecast.iloc[-period_forecast:-1].yhat)
d_returns = d_returns.reset_index(drop=True)
print(d_returns)

ax = d_returns.plot()

prediction.plot(ax=ax)

plt.show()

result_df = pd.DataFrame()
result_df['real'] = d_returns['y']
result_df['prediction'] = prediction['y']
result_df['Error'] = result_df['real'].sub(result_df['prediction'], axis = 0)

result_df['Error'].plot()
plt.show()
abs(result_df['Error']).plot()
plt.show()


