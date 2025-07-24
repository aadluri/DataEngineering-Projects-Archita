# Weather ETL Pipelin

An end-to-end data engineering and analytics pipeline. For personal skill development mainly
Should get and save Weather data, and send personalized updates to a phone - can be personalized for people in different areas Like friends or family members. 
Will be using: 
- Airflow for orchestration ( can also use cron to run daily)
- PostgreSQL for storage
- dbt for transformation
- Streamlit dashboard for weather insights

## Features

- Daily data fetch from OpenWeatherMap
- Loads to PostgreSQL
- Transforms with dbt
- Interactive dashboard with Streamlit

## How to Run

1. Set up Airflow scheduler and run the DAG
2. Run dbt with `dbt run`
3. Launch dashboard: `streamlit run dashboard/app.py`
