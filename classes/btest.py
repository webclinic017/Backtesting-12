import pandas as pd
import matplotlib.pyplot as plt


class backtest():
    def __init__(self, d_returns, prediction):
        self.d_returns = d_returns
        self.prediction = prediction

    def print_graph(self):
        ax = self.d_returns.plot()

        self.prediction.plot(ax=ax)

        plt.show()
    def error_graph(self):
        result_df = pd.DataFrame()
        result_df['real'] = self.d_returns['y']
        result_df['prediction'] = self.prediction['y']
        result_df['Error'] = result_df['real'].sub(result_df['prediction'], axis = 0)

        result_df['Error'].plot()
        plt.show()
        abs(result_df['Error']).plot()
        plt.show()
