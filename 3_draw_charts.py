import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter
import csv
from datetime import datetime
from config import SYMBOLS
from log_config import logger


def generate_stock_chart_high_prices_with_volume():
    logger.info("Generate stock chart START")

    for symbol in SYMBOLS:
        # Define file paths
        csv_file_path = f"data/{symbol}_historical.csv"
        image_file_path = f"static/images/{symbol}_high_prices_with_volume.png"

        # Initialize lists to hold data
        dates = []
        highs = []
        volumes = []

        # Read the CSV file
        with open(csv_file_path, newline="") as csvfile:
            csvreader = csv.reader(csvfile)
            # Skip header row
            next(csvreader)
            for row in csvreader:
                date_str = row[0]
                high_price = float(row[2])
                volume = int(row[6]) / 1e6  # Convert volume to millions
                # Convert date string to datetime object
                date = datetime.strptime(date_str, "%Y-%m-%d")
                dates.append(date)
                highs.append(high_price)
                volumes.append(volume)

        # Create a figure and a set of subplots
        fig, ax1 = plt.subplots(
            figsize=(15, 4)
        )  # Wider and shorter figure size

        # Plot high prices on the first y-axis
        ax1.plot(dates, highs, marker=",", color="g", label="High Prices")
        ax1.set_title(f"High Prices and Volume for {symbol}", fontsize=12)
        ax1.set_ylabel("High Price (USD)", fontsize=10, color="0.6")
        ax1.tick_params(axis="y", labelcolor="0.6")
        ax1.grid(True, linestyle="--", alpha=0.3)  # Lighter grid lines

        # Format the y-axis labels for high prices as USD
        ax1.yaxis.set_major_formatter(StrMethodFormatter("${x:,.2f}"))

        # Create a second y-axis to plot the volume data
        ax2 = ax1.twinx()
        ax2.bar(dates, volumes, alpha=0.3, color="0.1", label="Volume")
        ax2.set_ylabel("Volume (Millions)", fontsize=10, color="0.6")
        ax2.tick_params(axis="y", labelcolor="0.6")

        # Format the y-axis labels for volume to show numbers in millions
        ax2.yaxis.set_major_formatter(StrMethodFormatter("{x:.1f}M"))

        # Save the plot as an image file
        plt.savefig(image_file_path)
        plt.close()

        logger.info(
            "%s - generated and saved an image with volume",
            symbol,
        )

    logger.info("Generated stock charts for %s", SYMBOLS)
    logger.info("Generate stock chart END")


def generate_stock_chart_high_prices():

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

        # Set the figure size (e.g., 10 inches wide and 4 inches high)
        plt.figure(figsize=(15, 4))  # Wider and shorter figure size
        plt.plot(
            dates,
            highs,
            marker=",",
            # color="r",
        )
        plt.title(f"High Prices for {symbol}", fontsize=12)
        # plt.xlabel("Date", fontsize=10)
        # plt.ylabel("High Price", fontsize=10)
        plt.grid(True, linestyle="--", alpha=0.7)  # Lighter grid lines

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
    generate_stock_chart_high_prices()
    generate_stock_chart_high_prices_with_volume()
