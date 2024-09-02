import requests
from bs4 import BeautifulSoup
import json


def fetch_stock_data(symbols):
    stock_data = {}

    for symbol in symbols:
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
                change_percent_element.get_text(strip=True)
                if change_percent_element
                else "N/A"
            ),
            "volume": (
                volume_element.get_text(strip=True)
                if volume_element
                else "N/A"
            ),
        }

    return stock_data


def main():
    symbols = ["BTC-USD", "TSLA"]
    stock_data = fetch_stock_data(symbols)
    with open("stock_data.json", "w") as file:
        json.dump(stock_data, file, indent=4)


if __name__ == "__main__":
    main()
