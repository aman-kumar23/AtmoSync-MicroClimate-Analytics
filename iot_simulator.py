import csv
import json
import random
import time
from datetime import datetime

CONTAINERS = [
    {
        "container_id": "CONT_IN_101",
        "commodity": "Avocados",
        "origin": "Mumbai Port",
        "dest_primary": "Delhi Hub",
        "dest_secondary": "Jaipur Hub",
    },
    {
        "container_id": "CONT_IN_102",
        "commodity": "Berries",
        "origin": "Bengaluru",
        "dest_primary": "Hyderabad",
        "dest_secondary": "Vijayawada",
    },
    {
        "container_id": "CONT_IN_103",
        "commodity": "Bananas",
        "origin": "Kochi",
        "dest_primary": "Chennai",
        "dest_secondary": "Madurai",
    },
]


def generate_telemetry_reading():
    container = random.choice(CONTAINERS)
    base_temp = random.choice([3.0, 8.0, 15.0, 22.0])
    temp_spike = round(random.uniform(-1.0, 6.0), 2)
    current_temp = round(base_temp + temp_spike, 2)

    return {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "container_id": container["container_id"],
        "commodity": container["commodity"],
        "origin": container["origin"],
        "destination_primary": container["dest_primary"],
        "destination_secondary": container["dest_secondary"],
        "temperature_c": current_temp,
        "humidity_percent": round(random.uniform(55.0, 92.0), 2),
        "vibration_g": round(random.uniform(0.1, 2.8), 2),
    }


# Generate 100 sample records to CSV
csv_filename = "iot_sensor_telemetry.csv"
fieldnames = [
    "timestamp",
    "container_id",
    "commodity",
    "origin",
    "destination_primary",
    "destination_secondary",
    "temperature_c",
    "humidity_percent",
    "vibration_g",
]

with open(csv_filename, mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for _ in range(5000):
        writer.writerow(generate_telemetry_reading())

print(
    f"Successfully generated 5000 IoT records in '{csv_filename}' for AtmoSync Project!"
)