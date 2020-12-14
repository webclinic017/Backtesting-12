from fbprophet import Prophet
from fbprophet.diagnostics import cross_validation
from fbprophet.diagnostics import performance_metrics
from fbprophet.plot import plot_cross_validation_metric
import matplotlib.pyplot as plt
import pandas as pd




class forecast():
    def __init__(self, train, period_forecast):
        self.train = train
        self.period_forecast = period_forecast
        self.prophet = Prophet(changepoint_prior_scale=0.15, daily_seasonality=False)

    def predict(self):

        self.prophet.fit(self.train)


        build_forecast = self.prophet.make_future_dataframe(periods=self.period_forecast, freq='D')

        self.forecast = self.prophet.predict(build_forecast)
        return forecast


    def print_details(self):
        # tell us more about the forecast
        self.prophet.plot_components(self.forecast)
        plt.show()



    def get_predictions(self):
        print(self.forecast.iloc[-self.period_forecast:-1].yhat)
        prediction = pd.DataFrame()
        prediction['y'] = (self.forecast.iloc[-self.period_forecast:-1].yhat)
        return prediction
