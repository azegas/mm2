import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter
import csv
from datetime import datetime
from config import SYMBOLS
from log_config import logger
import os
from dotenv import load_dotenv

load_dotenv()
base_dir = os.getenv("BASE_DIR")

def generate_stock_chart_high_prices_with_volume():
    logger.info("##########################################################")
    logger.info("Generate stock chart START")


    for symbol in SYMBOLS:
        # Define file paths
        csv_file_path = os.path.join(base_dir, f"data/{symbol}_historical.csv")
        image_file_path = os.path.join(base_dir, f"static/images/{symbol}_high_prices_with_volume.png")

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

        # Create a figure and a set of subplots with a black background
        fig, ax1 = plt.subplots(figsize=(15, 4), facecolor='black')
        ax1.set_facecolor('black')  # Set the facecolor of the axis

        # Plot high prices on the first y-axis
        ax1.plot(dates, highs, marker=",", color="white", label="High Prices")
        ax1.set_title(f"High Prices and Volume for {symbol}", fontsize=15, color='white')
        ax1.set_ylabel("High Price (USD)", fontsize=15, color="white")
        ax1.tick_params(axis="y", labelcolor="white", labelsize=15)
        ax1.tick_params(axis="x", labelcolor="white", labelsize=15)
        ax1.grid(True, linestyle="--", alpha=0.5, color='gray')  # Lighter grid lines

        # Format the y-axis labels for high prices as USD
        ax1.yaxis.set_major_formatter(StrMethodFormatter("${x:,.2f}"))

        # Create a second y-axis to plot the volume data
        ax2 = ax1.twinx()
        ax2.bar(dates, volumes, alpha=0.3, color="gray", label="Volume")
        ax2.set_ylabel("Volume (Millions)", fontsize=15, color="white")
        ax2.tick_params(axis="y", labelcolor="white", labelsize=15)

        # Format the y-axis labels for volume to show numbers in millions
        ax2.yaxis.set_major_formatter(StrMethodFormatter("{x:.1f}M"))

        # Set the background color of the plot area to black
        ax1.set_facecolor('black')
        ax2.set_facecolor('black')

        # Save the plot as an image file with a transparent background
        plt.savefig(image_file_path, bbox_inches='tight', facecolor='black', edgecolor='none')
        plt.close()

        logger.info(
            "%s - generated and saved an image with volume",
            symbol,
        )

    logger.info("Generated stock charts for %s", SYMBOLS)
    logger.info("Generate stock chart END")

if __name__ == "__main__":
    generate_stock_chart_high_prices_with_volume()
