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
print("\n Data Cleaning & Preprocessing Successful  ")
print(f"Total processed telemetry rows: {len(telemetry_df)}")

# 5. Drop duplicate rows and validate telemetry numeric ranges
telemetry_df = telemetry_df.drop_duplicates()
pricing_df = pricing_df.drop_duplicates()

if 'temperature_c' in telemetry_df.columns:
    before_temp_filter = len(telemetry_df)
    telemetry_df = telemetry_df[telemetry_df['temperature_c'].between(-40, 60)]
    print(f"\nFiltered out-of-range temperature rows: {before_temp_filter - len(telemetry_df)}")

print(f"Final telemetry rows after cleaning: {len(telemetry_df)}")
print(f"Final pricing rows after cleaning: {len(pricing_df)}")