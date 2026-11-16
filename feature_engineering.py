import pandas as pd

# 1. Load datasets
telemetry_df = pd.read_csv('iot_sensor_telemetry.csv')
pricing_df = pd.read_csv('Commodity_pricing.csv')

# 2. Merge telemetry data with pricing data based on 'commodity'
merged_df = pd.merge(telemetry_df, pricing_df, on='commodity', how='inner')

# 3. Calculate Spoilage Risk
# Check if current temperature exceeds the threshold temperature
merged_df['temp_exceeded'] = merged_df['temperature_c'] - merged_df['threshold_temp_c']
merged_df['spoilage_risk_score'] = merged_df.apply(
    lambda row: max(0, row['temp_exceeded'] * row['spoilage_rate_per_deg_hr']) if row['temp_exceeded'] > 0 else 0,
    axis=1
)

# 4. Calculate Market Arbitrage (Price difference between secondary and primary markets)
merged_df['arbitrage_margin_per_kg'] = merged_df['secondary_market_price_per_kg'] - merged_df['primary_market_price_per_kg']

# 5. Display sample insights
print(" Feature Engineering & Analytics Sample")
print(merged_df[['container_id', 'commodity', 'temperature_c', 'threshold_temp_c', 'spoilage_risk_score', 'arbitrage_margin_per_kg']].head(5))