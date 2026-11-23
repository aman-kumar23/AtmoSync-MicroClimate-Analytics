import pandas as pd

# Load IoT telemetry and commodity pricing datasets
telemetry_df = pd.read_csv('iot_sensor_telemetry.csv')
pricing_df = pd.read_csv('Commodity_pricing.csv')

print(" IoT Telemetry Data Info ")
print(telemetry_df.info())

print("\n Commodity Pricing Data Info ")
print(pricing_df.info())
processed_df = pd.read_csv('processed_atmosync_data.csv')

print("\n=== Top High-Risk Containers ===")
container_summary = (
    processed_df.groupby(['container_id', 'commodity'], as_index=False)
    .agg(
        avg_temp_c=('temperature_c', 'mean'),
        avg_threshold_c=('threshold_temp_c', 'mean'),
        avg_spoilage_risk=('spoilage_risk_score', 'mean'),
        avg_arbitrage_margin=('arbitrage_margin_per_kg', 'mean'),
    )
    .sort_values(by='avg_spoilage_risk', ascending=False)
)
print(container_summary.head(10).to_string(index=False))

print("\n Commodity Spoilage & Arbitrage Summary")
commodity_summary = (
    processed_df.groupby('commodity', as_index=False)
    .agg(
        records=('container_id', 'count'),
        avg_spoilage_risk=('spoilage_risk_score', 'mean'),
        avg_arbitrage_margin=('arbitrage_margin_per_kg', 'mean'),
    )
    .sort_values(by='avg_spoilage_risk', ascending=False)
)
print(commodity_summary.to_string(index=False))