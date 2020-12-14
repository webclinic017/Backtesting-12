from classes.data import data
from classes.predict import forecast
from classes.btest import backtest

def main():
    dataset = data("AAPL", "2010-01-01", "2018-03-01", 0.95)
    dataset.load_data()


    future = forecast(dataset.load_data(), dataset.get_periods())
    future.predict()

    future.print_details()


    results = backtest(dataset.get_all_returns(), future.get_predictions())
    results.print_graph()
    results.error_graph()


if __name__ == "__main__":
    main()

