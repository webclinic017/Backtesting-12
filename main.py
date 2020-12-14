from classes.data import data
from classes.predict import forecast
from classes.btest import backtest

def main():
    test = data()
    test.load_data()
    #print(test.load_data())
    # create object here 
    test2 = forecast(test.load_data(), test.get_periods())
    test2.predict()
    #test2.print_details()
    test2.get_predictions()
    test3 = backtest(test.get_all_returns(), test2.get_predictions())
    test3.print_graph()
    test3.error_graph()
if __name__ == "__main__":
    main()

