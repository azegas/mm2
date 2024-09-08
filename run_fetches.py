from fetches.invest_fetch_stock_data import fetch_stock_data
# from fetches.invest_fetch_historical_data import fetch_historical_data
# from fetches.invest_draw_charts import generate_stock_chart_high_prices_with_volume
from fetches.cvbankas import fetch_cvbankas_jobs

def run_all_fetches():
    try:
        fetch_cvbankas_jobs()
        fetch_stock_data()
        # fetch_historical_data()
        # generate_stock_chart_high_prices_with_volume()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        # If any fetch fails, we don't continue with the others
        return

if __name__ == "__main__":
    run_all_fetches()