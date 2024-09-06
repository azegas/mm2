from flask import Flask, jsonify, send_from_directory
import os
import json
import os
from dotenv import load_dotenv

load_dotenv()
base_dir = os.getenv("BASE_DIR")

app = Flask(__name__)


@app.route("/")
def home():
    return send_from_directory("static", "index.html")


@app.route("/read_stock_data_from_file")
def stock_data():
    file_path = os.path.join(base_dir, "data/stock_data.json")
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            data = json.load(file)
        return jsonify(data)
    else:
        return jsonify({"error": "Data not found"}), 404


if __name__ == "__main__":
    app.run(
        debug=True
    )
