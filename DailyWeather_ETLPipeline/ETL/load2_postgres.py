import json
import psycopg2
from datetime import datetime

conn = psycopg2.connect("dbname=weather user=username password=yourpass")

def load2_database(json_path):
    with open(json_path, 'r') as file:
        data = json.load(file)

    cursor = conn.cursor()
    
    for record in data:
        date = datetime.strptime(record['date'], '%Y-%m-%d')
        temperature = record['temperature']
        humidity = record['humidity']
        wind_speed = record['wind_speed']
        
        cursor.execute("""
            INSERT INTO raw_weather_data (date, temperature, humidity, wind_speed)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (date) DO UPDATE SET
                temperature = EXCLUDED.temperature,
                humidity = EXCLUDED.humidity,
                wind_speed = EXCLUDED.wind_speed;
        """, (date, temperature, humidity, wind_speed))
    
    conn.commit()
    cursor.close()