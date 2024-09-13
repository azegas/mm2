import psutil
from gpiozero import CPUTemperature
import json
from datetime import datetime
import os

def get_system_info():
    cpu = psutil.cpu_percent(interval=1)  # Get CPU usage over 1 second
    memory = psutil.virtual_memory().percent
    temp = CPUTemperature().temperature
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {
        "timestamp": date,
        "cpu_usage": cpu,
        "memory_usage": memory,
        "temperature": temp
    }

def save_to_file(data, filename="data/system_info.json"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def fetch_raspberry_system_info():
    info = get_system_info()
    save_to_file(info)

def main():
    fetch_raspberry_system_info()

if __name__ == "__main__":
    main()