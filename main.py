from classes.data import Data
from classes.predict import Prophesy
from classes.btest import Backtest
from classes.dataex import Explore
from rich import print
from rich.console import Console
from rich.table import Table

def main():
    while True:
      table = Table(title="Menu")
      table.add_column("Selection", justify="center", style="white", no_wrap=True)
      table.add_column("Action", justify="left", style="yellow") 
      table.add_row("1.", "Load data")
      table.add_row("2.", "Explore data")
      table.add_row("3.", "Predict future")
      table.add_row("4.", "Display results")
      table.add_row("5.", "Predict without backtesting")
      table.add_row("0.", "Exit")
      console = Console()
      console.print(table)

      __choose_menu = int(input("Enter your choice: "))
      if __choose_menu == 1:
        user = input("Enter Stock ticker: ")
        start_date = input("Enter start date yyyy-mm-dd: ")
        end_date = input("Enter end date yyyy-mm-dd: ")
        ratio = float(input("Percentage of how much data should be predicted (0-1), \ne.g. 0.95 indicates that 5% of provided data will be predicted: "))
        dataset = Data(f'{user}', f'{start_date}', f'{end_date}', ratio)
        dataset.load_data()
      elif __choose_menu == 2:
        explore = Explore(dataset.original_data()['Adj Close'])
        explore.time_series_decomposition(3)
      elif __choose_menu == 3:
        future = Prophesy(dataset.load_data(), dataset.get_periods())
        future.predict_future()
      elif __choose_menu == 4:
        results = Backtest(dataset.get_all_returns(), future.get_predictions())
        results.print_graph()
        results.error_graph()
      elif __choose_menu == 5:
        user = input("Enter Stock ticker: ")
        future_days = int(input("Enter days to predict: "))
        start_date = input("Enter start date yyyy-mm-dd: ")
        end_date = input("Enter end date yyyy-mm-dd: ")
        dataset = Data(f'{user}', f'{start_date}',f'{end_date}', 1)
        dataset.load_data()
        future = Prophesy(dataset.get_prepared_data(), future_days)
        results = future.predict_future()
        future.plot_result(results)
        future.plot_only_predictions(results, future_days) 
      elif __choose_menu == 0:
        exit(0)
      else:
        print ("Invalid Choice")

if __name__ == "__main__":
    main()

