# AtmoSync: Micro-Climate Arbitrage Analytics

## Project Overview
An advanced data analytics project focused on evaluating IoT sensor telemetry data alongside commodity pricing to identify micro-climate arbitrage opportunities and supply chain impacts.

## Deliverables & Scope
* IoT Sensor Telemetry Analysis: Tracking container conditions (temperature, humidity, vibration) during transit across primary and secondary corridors.

* Commodity Price Impact: Assessing price fluctuations and spoilage risks for agricultural commodities (Avocados, Berries, Bananas, Mangoes).

* Automation & Scripting: Python-based simulation iot_simulator.py generating telemetry logs.

## Pipeline & Key Metrics
* Data Cleaning (data_cleaning.py): Checks for missing values, parses timestamps, checks duplicate telemetry rows, and      validates temperature ranges across 5000 telemetry rows and 4 pricing rows.

* Feature Engineering (feature_engineering.py): Merges telemetry and pricing data, calculates spoilage_risk_score and arbitrage_margin_per_kg , groups spoilage_risk_tier (Low, Medium, High), and saves processed_atmosync_data.csv.

* Analytics Summary (data_analysis.py): Prints dataset info along with top high-risk containers and commodity-wise spoilage and arbitrage summaries.

* Power BI Dashboard (Atmosync-microclimate-dashboard.pbix): Visualizes container micro-climate trends, risk tiers, and market arbitrage opportunities.