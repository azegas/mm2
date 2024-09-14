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

def read_random_quote():
    file_path = os.path.join(base_dir, "data/random_quote.json")
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            data = json.load(file)
            return data
    return {"error": "Data not found"}


# SocketIO Event Handlers (BACKEND, SERVER)
# Listening for incoming connections such as `server_give_me_stock_data`
# and sending back the data(that we received over `read_stock_data`) 
# to the client over `client_here_is_stock_data`

@socketio.on('connect')
def event_handler_connect():
    """
    Event handler for client connection.
    When a client connects, it sends initial data for all components.
    """
    emit('client_here_is_stock_data', read_stock_data())
    emit('client_here_is_cvbankas_data', read_cvbankas_data())
    emit('client_here_is_sensor_data', read_sensor_data())
    emit('client_here_is_test_data', read_test_data())

@socketio.on('server_give_me_stock_data')
def event_handler_stock():
    emit('client_here_is_stock_data', read_stock_data())

@socketio.on('server_give_me_sensor_data')
def event_handler_sensor():
    emit('client_here_is_sensor_data', read_sensor_data())

@socketio.on('server_give_me_cvbankas_data')
def event_handler_cvbankas():
    emit('client_here_is_cvbankas_data', read_cvbankas_data())

@socketio.on('server_give_me_system_info')
def event_handler_system_info():
    emit('client_here_is_system_info', read_system_info())

@socketio.on('server_give_me_random_quote')
def event_handler_random_quote():
    emit('client_here_is_random_quote', read_random_quote())

@socketio.on('server_give_me_test_data')
def event_handler_test():
    emit('client_here_is_test_data', read_test_data())

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    # Run the Flask application with SocketIO
    socketio.run(app, debug=True, host='0.0.0.0', port=5000, 
                 allow_unsafe_werkzeug=True # so could run as a service
                 )
