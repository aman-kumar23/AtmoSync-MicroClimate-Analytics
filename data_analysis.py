import pandas as pd

# Load IoT telemetry and commodity pricing datasets
telemetry_df = pd.read_csv('iot_sensor_telemetry.csv')
pricing_df = pd.read_csv('Commodity_pricing.csv')

print(" IoT Telemetry Data Info ")
print(telemetry_df.info())

print("\n Commodity Pricing Data Info ")
print(pricing_df.info())