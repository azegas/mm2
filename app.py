from flask import Flask, jsonify, send_from_directory
import os
import json
import time

app = Flask(__name__)


@app.route("/")
def home():
    return send_from_directory("static", "index.html")


@app.route("/read_stock_data_from_file")
def stock_data():
    file_path = "stock_data.json"
    if os.path.exists(file_path):
        # Get the last modified time
        last_modified = os.path.getmtime(file_path)
        last_modified_str = time.strftime(
            "%Y-%m-%d %H:%M:%S", time.localtime(last_modified)
        )

        response = {"timestamp": last_modified_str, "data": {}}

        with open(file_path, "r") as file:
            response["data"] = json.load(file)

        return jsonify(response)
    else:
        return jsonify({"error": "Data not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
