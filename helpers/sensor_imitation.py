import json
import random
import time
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

base_dir = os.getenv("BASE_DIR")

def generate_sensor_data():
    temperature = round(random.uniform(15, 35), 1)  # Temperature between 15°C and 35°C
    humidity = round(random.uniform(30, 90), 1)  # Humidity between 30% and 90%
    last_update = datetime.now().strftime("%H:%M")
    return {"temperature": temperature, "humidity": humidity, "last_update": last_update}

def write_to_file():
    while True:
        sensor_data = generate_sensor_data()
        file_path = os.path.join(base_dir, "data/sensor_data.json")
        with open(file_path, "w") as file:
            json.dump(sensor_data, file, indent=4)
        print(f"Updated sensor data: Temperature {sensor_data['temperature']}°C, Humidity {sensor_data['humidity']}%, Last Update: {sensor_data['last_update']}")
        time.sleep(2)

if __name__ == "__main__":
    write_to_file()
