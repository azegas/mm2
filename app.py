from flask import Flask, jsonify, send_from_directory
import os
import json
import os
from dotenv import load_dotenv

load_dotenv()
base_dir = os.getenv("BASE_DIR")

# Initialize a Flask application
app = Flask(__name__)


# Route for the home page, serves the index.html file from the "static" directory
@app.route("/")
def home():
    return send_from_directory("static", "index.html")


# Route to read stock data from a JSON file and return it as a JSON response
@app.route("/read_stock_data_from_file")
def stock_data():
    file_path = os.path.join(base_dir, "data/stock_data.json")
    if os.path.exists(file_path):
        # Open the JSON file and load its contents
        with open(file_path, "r") as file:
            data = json.load(file)  # Parse the JSON data

        # Return the parsed data as a JSON response
        return jsonify(data)
    else:
        # If the file doesn't exist, return an error message with a 404 status
        return jsonify({"error": "Data not found"}), 404


# Run the Flask application only if this script is executed directly
if __name__ == "__main__":
    app.run(
        debug=True
    )  # Start the Flask development server with debug mode enabled
