from classes.data import Data
from classes.predict import Prophesy
from classes.btest import Backtest

def main():
    #dataset = data("AAPL", "2010-01-01", "2018-03-01", 0.95)
    dataset = Data("GOOGL", "2010-01-01", "2018-03-01", 0.95)
    dataset.load_data()


    future = Prophesy(dataset.load_data(), dataset.get_periods())
    future.predict_future()

    future.print_details()


    results = Backtest(dataset.get_all_returns(), future.get_predictions())
    results.print_graph()
    results.error_graph()


if __name__ == "__main__":
    main()

