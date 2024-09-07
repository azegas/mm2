import requests
from config import (
    SYMBOLS,
    HISTORICAL_URL,
    START_DATE_UNIX,
    END_DATE_UNIX,
    START_DATE_HUMAN,
    END_DATE_HUMAN,
)
from log_config import logger
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

# getting 429 status code. Adding headers is a fix for it.
# User-Agent Identification: Servers may restrict access based on the
# User-Agent header, which identifies the client making the request.
# Browsers often include a User-Agent that might be more trusted than the d
# efault one used by scripts.
# Solution: Mimic a browser's User-Agent header in your script
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}


def fetch_historical_data():
    
    logger.info("##########################################################")
    logger.info(
        "Fetch historical for %s from %s to %s START",
        SYMBOLS,
        START_DATE_HUMAN,
        END_DATE_HUMAN,
    )

    for symbol in SYMBOLS:
        csv_url = f"{HISTORICAL_URL}{symbol}?period1={str(int(START_DATE_UNIX))}&period2={str(int(END_DATE_UNIX))}&interval=1d&events=history&includeAdjustedClose=true"
        base_dir = os.getenv("BASE_DIR")
        file_path = os.path.join(base_dir, f"data/{symbol}_historical.csv")

        breakpoint()

        try:
            # Make the request with headers
            response = requests.get(csv_url, headers=headers)

            if response.status_code == 200:
                # Save the content to a file
                with open(file_path, "wb") as file:
                    file.write(response.content)
                logger.info(
                    "%s - File downloaded and saved to %s", symbol, file_path
                )
            else:
                logger.error(
                    "%s - failed to download file. Status code: %s",
                    symbol,
                    response.status_code,
                )
                return  # Exit the function if any symbol fails

        except requests.exceptions.RequestException as e:
            logger.error(f"An error occurred: {e}")
            return  # Exit the function if any exception occurs

    logger.info("Successfully fetched historical data for all symbols")


def main():
    fetch_historical_data()


if __name__ == "__main__":
    main()
