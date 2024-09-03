import matplotlib.pyplot as plt
import csv
from datetime import datetime
from config import SYMBOLS
from log_config import logger


def generate_stock_chart():

    logger.info("Generate stock chart START")

    for symbol in SYMBOLS:
        # Define file paths
        csv_file_path = f"data/{symbol}_historical.csv"
        image_file_path = f"static/images/{symbol}_high_prices.png"

        # Initialize lists to hold data
        dates = []
        highs = []

        # Read the CSV file
        with open(csv_file_path, newline="") as csvfile:
            csvreader = csv.reader(csvfile)
            # Skip header row
            next(csvreader)
            for row in csvreader:
                date_str = row[0]
                high_price = float(row[2])
                # Convert date string to datetime object
                date = datetime.strptime(date_str, "%Y-%m-%d")
                dates.append(date)
                highs.append(high_price)

        # Plot the 'High' prices
        # Set the figure size (e.g., 10 inches wide and 4 inches high)
        # Plot the 'High' prices
        plt.figure(figsize=(18, 2))  # Wider and shorter figure size
        plt.plot(
            dates,
            highs,
            marker="o",
            linestyle="-",
            color="b",
            linewidth=1,
            markersize=1,
        )  # Thinner line and smaller markers
        plt.title(f"High Prices for {symbol}", fontsize=12)
        plt.xlabel("Date", fontsize=10)
        plt.ylabel("High Price", fontsize=10)
        plt.grid(True, linestyle="--", alpha=0.7)  # Lighter grid lines
        plt.tight_layout()  # Adjust layout to fit labelsplt.figure(figsize=(10, 2))
        plt.plot(dates, highs, marker="o", linestyle="-", color="b")
        plt.title(f"High Prices for {symbol}")
        plt.xlabel("Date")
        plt.ylabel("High Price")
        plt.grid(True)

        # Save the plot as an image file
        plt.savefig(image_file_path)
        plt.close()

        logger.info(
            "%s - generated and saved an image",
            symbol,
        )

    logger.info("Generated stock charts for %s", SYMBOLS)
    logger.info("Generate stock chart END")


if __name__ == "__main__":
    generate_stock_chart()
