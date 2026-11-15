import pandas as pd

# 1. Load datasets
telemetry_df = pd.read_csv('iot_sensor_telemetry.csv')
pricing_df = pd.read_csv('Commodity_pricing.csv')

print(" Missing Values Check ")
print("Telemetry Missing Values:\n", telemetry_df.isnull().sum())
print("\nPricing Missing Values:\n", pricing_df.isnull().sum())

# 2. Convert timestamp to actual datetime format
telemetry_df['timestamp'] = pd.to_datetime(telemetry_df['timestamp'])

# 3. Check for duplicate rows
telemetry_duplicates = telemetry_df.duplicated().sum()
print(f"\nDuplicate rows in Telemetry: {telemetry_duplicates}")

# 4. Basic summary after cleaning steps
print("\n Data Cleaning & Preprocessing Successful ")
print(f"Total processed telemetry rows: {len(telemetry_df)}")