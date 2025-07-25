# Weather ETL Pipelin

An end-to-end data engineering and analytics pipeline. For personal skill development mainly.  Used jupyter notebook to keep my notes and code together. 
Should get and save weather data, and send personalized updates to a phone - can be personalized for people in different areas Like friends or family members. 

get weather api here: https://www.weatherapi.com/signup.aspx 

Can also use https://open-meteo.com/ (will need to update *fetch_weather_daily()* )

Will be using: 
- Airflow for orchestration (also use cron to run daily)
- PostgreSQL for storage
- dbt for transformation 
- Streamlit dashboard for weather insights

create a dbt project by running in terminal
> dbt init weather_dbt

## How to Run

Set up Airflow scheduler and run the DAG - working on CRON jobs
Run dbt with `dbt run`
Launch dashboard: `streamlit run dashboard/app.py`
