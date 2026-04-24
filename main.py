# C6: Main workflow for application
# This file:
# 1. Creates WeatherData object for a specific location and date
# 2. Retrieves and processes weather data from Open-Meteo API
# 3. Stores calculated results in SQLite Database using SQAlchemy
# 4. Queries the database to verify that the data was stored correctly
from weather import WeatherData
from database import engine, WeatherTable
from sqlalchemy.orm import sessionmaker

# Creates database session to interact with SQLite database
Session = sessionmaker(bind=engine)
session = Session()

# Creates WeatherData object for Chattanooga, TN on November 15, 2025
chattanooga = WeatherData(35.0456, -85.3097,11, 15, 2025)

# Retrieves and calculates weather statistics using the API
chattanooga.get_temperature_data()
chattanooga.get_wind_data()
chattanooga.get_precipitation_data()

# Creates a database record using the calculated weather data
record = WeatherTable(
    latitude=chattanooga.latitude,
    longitude=chattanooga.longitude,
    month=chattanooga.month,
    day=chattanooga.day,
    year=chattanooga.year,

    avg_temp=chattanooga.avg_temp,
    min_temp=chattanooga.min_temp,
    max_temp=chattanooga.max_temp,

    avg_wind=chattanooga.avg_wind,
    min_wind=chattanooga.min_wind,
    max_wind=chattanooga.max_wind,

    sum_precip=chattanooga.sum_precip,
    min_precip=chattanooga.min_precip,
    max_precip=chattanooga.max_precip
)

# Adds the record to the database and commits the transaction
session.add(record)
session.commit()

# Queries the database for the most recently inserted record
result = session.query(WeatherTable).order_by(WeatherTable.id.desc()).first()

# Displays stored weather statistics to confirm successful storage and retrieval
print("Temperature average:", result.avg_temp)
print("Temperature minimum:", result.min_temp)
print("Temperature maximum:", result.max_temp)

print("Wind speed average:", result.avg_wind)
print("Wind speed minimum:", result.min_wind)
print("Wind speed maximum:", result.max_wind)

print("Precipitation sum:", result.sum_precip)
print("Precipitation minimum:", result.min_precip)
print("Precipitation maximum:", result.max_precip)