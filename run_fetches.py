from fetch_stock_data import fetch_stock_data
from fetch_historical_data import fetch_historical_data
from draw_charts import generate_stock_chart_high_prices_with_volume

def run_all_fetches():
    fetch_stock_data()
    fetch_historical_data()
    generate_stock_chart_high_prices_with_volume()


if __name__ == "__main__":
    run_all_fetches()