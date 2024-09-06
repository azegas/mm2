from fetches.invest_fetch_stock_data import fetch_stock_data
from fetches.invest_fetch_historical_data import fetch_historical_data
from fetches.invest_draw_charts import generate_stock_chart_high_prices_with_volume
from fetches.cvbankas import fetch_cvbankas_jobs

def run_all_fetches():
    fetch_stock_data()
    fetch_historical_data()
    generate_stock_chart_high_prices_with_volume()
    fetch_cvbankas_jobs()


if __name__ == "__main__":
    run_all_fetches()