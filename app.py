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


# ------------------------------
# Functions to be used
# ------------------------------

def read_test_data():
    data = {
        "text": "testLOLOLO"
    }
    return data

def read_stock_data():
    file_path = os.path.join(base_dir, "data/stock_data.json")
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            data = json.load(file)
            return data
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
            data = json.load(file)
            return data
    return {"error": "Data not found"}

def read_system_info():
    file_path = os.path.join(base_dir, "data/system_info.json")
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            data = json.load(file)
            return data
    return {"error": "Data not found"}


# ------------------------------
# SocketIO Event Handlers
# 
# The following section defines event handlers for various SocketIO events,
# which facilitate real-time updates between the server and connected clients.
# ------------------------------
    
# TODO Check the size of the data you're emitting in your Socket.IO event handlers. 
# TODO If the data is too big, the client might not be able to handle it and the connection might be dropped.
# TODO Consider using chunking or streaming to send the data in smaller chunks.
# Jo, taip buna, kai serveriukas nepasileidiza tiesiog.
@socketio.on('connect') # event handler
def handle_connect(): # function to be called when the event handler is triggered
    emit('stock_display_refresh', read_stock_data()) # emit is used to send data to the client
    emit('cvbankas_display_refresh', read_cvbankas_data())
    emit('sensor_display_refresh', read_sensor_data())
    emit('test_display_refresh', read_test_data())

@socketio.on('request_stock_update')
def handle_stock_update_request():
    emit('stock_display_refresh', read_stock_data())

@socketio.on('request_sensor_update')
def handle_sensor_update_request():
    emit('sensor_display_refresh', read_sensor_data())

@socketio.on('request_cvbankas_update')
def handle_cvbankas_update_request():
    emit('cvbankas_display_refresh', read_cvbankas_data())

@socketio.on('request_test_update')
def handle_test_update_request():
    emit('test_display_refresh', read_test_data())

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)
