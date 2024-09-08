from flask import Flask, jsonify, render_template
import os
import json
from dotenv import load_dotenv
from flask_socketio import SocketIO, emit
from log_config import logger

load_dotenv()
base_dir = os.getenv("BASE_DIR")

app = Flask(__name__)
socketio = SocketIO(app)

def read_stock_data():
    file_path = os.path.join(base_dir, "data/stock_data.json")
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return json.load(file)
    return {"error": "Data not found"}

def read_sensor_data():
    file_path = os.path.join(base_dir, "data/sensor_data.json")
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            data = json.load(file)
            return data
    logger.warning("Sensor data file not found")
    return {"error": "Data not found"}

def read_cvbankas_data():
    file_path = os.path.join(base_dir, "data/cvbankas_ads.json")
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return json.load(file)
    return {"error": "Data not found"}
    
@socketio.on('connect')
def handle_connect():
    emit('stock_display_refresh', read_stock_data())
    emit('cvbankas_display_refresh', read_cvbankas_data())
    emit('sensor_display_refresh', read_sensor_data())

@socketio.on('request_stock_update')
def handle_stock_update_request():
    emit('stock_display_refresh', read_stock_data())

@socketio.on('request_sensor_update')
def handle_sensor_update_request():
    emit('sensor_display_refresh', read_sensor_data())

@socketio.on('request_cvbankas_update')
def handle_cvbankas_update_request():
    emit('cvbankas_display_refresh', read_cvbankas_data())

@app.route("/")
def home():
    return render_template("index.html", initial_stock_data=read_stock_data(), initial_sensor_data=read_sensor_data())

if __name__ == "__main__":
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)
