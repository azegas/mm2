import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
from config import SYMBOLS
from log_config import logger
import os
from dotenv import load_dotenv

load_dotenv()

def fetch_stock_data():
    logger.info("Fetched stock data START")

    stock_data = {}
    fetch_time = datetime.now().strftime("%Y-%m-%d %H:%M")

    for symbol in SYMBOLS:
        url = f"https://finance.yahoo.com/quote/{symbol}/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        price_element = soup.find("fin-streamer", {"data-testid": "qsp-price"})
        change_element = soup.find(
            "fin-streamer", {"data-testid": "qsp-price-change"}
        )
        change_percent_element = soup.find(
            "fin-streamer", {"data-testid": "qsp-price-change-percent"}
        )
        volume_element = soup.find(
            "fin-streamer", {"data-field": "regularMarketVolume"}
        )
        one_year_estimate_element = soup.find(
            "fin-streamer", {"data-field": "targetMeanPrice"}
        )

        stock_data[symbol] = {
            "price": (
                price_element.get_text(strip=True) if price_element else "N/A"
            ),
            "change": (
                change_element.get_text(strip=True)
                if change_element
                else "N/A"
            ),
            "change_percent": (
                change_percent_element.get_text(strip=True).strip("()")
                if change_percent_element
                else "N/A"
            ),
            "volume": (
                volume_element.get_text(strip=True)
                if volume_element
                else "N/A"
            ),
            "one_year_estimate": (
                one_year_estimate_element.get_text(strip=True)
                if one_year_estimate_element
                else "N/A"
            ),
            "timestamp": fetch_time,  # Add the timestamp to each stock entry
        }

        logger.info(
            "%s - fetched stock data",
            symbol,
        )

    logger.info("Fetched stock data for %s", SYMBOLS)
    logger.debug("Stock data %s", stock_data)
    logger.info("Fetched stock data END")

    return stock_data


def main():
    stock_data = fetch_stock_data()

    base_dir = os.getenv("BASE_DIR")
        
    file_path = os.path.join(base_dir, "data/stock_data.json")

    with open(file_path, "w") as file:
        json.dump(stock_data, file, indent=4)


if __name__ == "__main__":
    main()
