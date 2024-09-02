import requests


# getting 429 status code. Adding headers is a fix for it.
# User-Agent Identification: Servers may restrict access based on the
# User-Agent header, which identifies the client making the request.
# Browsers often include a User-Agent that might be more trusted than the d
# efault one used by scripts.
# Solution: Mimic a browser's User-Agent header in your script
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}


def fetch_historical_data(symbols):
    for symbol in symbols:
        csv_url = f"https://query1.finance.yahoo.com/v7/finance/download/{symbol}?period1=1693658112&period2=1725280512&interval=1d&events=history&includeAdjustedClose=true"
        file_path = f"data/{symbol}_historical.csv"

        try:
            # Make the request with headers
            response = requests.get(csv_url, headers=headers)

            if response.status_code == 200:
                # Save the content to a file
                with open(file_path, "wb") as file:
                    file.write(response.content)
                print(f"File downloaded and saved to {file_path}")
            else:
                print(
                    f"Failed to download file for {symbol}. Status code: {response.status_code}"
                )

        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")


def main():
    symbols = ["TSLA", "TM"]
    fetch_historical_data(symbols)


if __name__ == "__main__":
    main()
