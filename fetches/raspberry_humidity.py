import time
import board
import adafruit_dht
import json
from datetime import datetime
import os

# + to pin 2 (5v)
# - to pin 6 (gnd)
# data to pin 7

# Define the sensor type (DHT22) and the pin it's connected to
DHT_PIN = board.D4  # This is GPIO4, which corresponds to physical pin 7 on Raspberry Pi 3B

# Initialize the DHT device
dht = adafruit_dht.DHT22(DHT_PIN)

print("DHT22 Test Program")
print("Press Ctrl+C to exit")

# Ensure the data directory exists
data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
os.makedirs(data_dir, exist_ok=True)

try:
    while True:
        try:
            # Read humidity and temperature
            humidity = dht.humidity
            temperature = dht.temperature

            if humidity is not None and temperature is not None:
                print(f"Temperature: {temperature:.1f}°C, Humidity: {humidity:.1f}%")
                
                # Prepare data to save
                sensor_data = {
                    "temperature": round(temperature, 1),
                    "humidity": round(humidity, 1),
                    "last_update": datetime.now().strftime("%H:%M:%S")
                }
                
                # Save data to JSON file
                with open(os.path.join(data_dir, 'sensor_data.json'), 'w') as f:
                    json.dump(sensor_data, f, indent=4)
            else:
                print("Failed to retrieve data from DHT22 sensor")

        except RuntimeError as e:
            # DHT22 sensors are sensitive, errors are common. We'll just print the error and try again.
            print(f"Reading error: {e.args[0]}")

        time.sleep(1)  # Wait for 1 second before the next reading

except KeyboardInterrupt:
    print("Program stopped by user")
finally:
    dht.exit()