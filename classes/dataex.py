import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt

class Explore():
    def __init__(self, data):
        self.data = data

    def time_series_decomposition(self, period):
        output = seasonal_decompose(self.data, model='multiplicative', period = period)
        output.plot().suptitle('Time series decomposition')
        plt.show()

        
