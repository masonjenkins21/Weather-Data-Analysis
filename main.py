from weather import WeatherData
from database import engine, WeatherTable
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()


chattanooga = WeatherData(35.0456, -85.3097,11, 15, 2025)

chattanooga.get_temperature_data()
chattanooga.get_wind_data()
chattanooga.get_precipitation_data()

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

session.add(record)
session.commit()

result = session.query(WeatherTable).order_by(WeatherTable.id.desc()).first()

print("Temperature average:", result.avg_temp)
print("Temperature minimum:", result.min_temp)
print("Temperature maximum:", result.max_temp)

print("Wind speed average:", result.avg_wind)
print("Wind speed minimum:", result.min_wind)
print("Wind speed maximum:", result.max_wind)

print("Precipitation sum:", result.sum_precip)
print("Precipitation minimum:", result.min_precip)
print("Precipitation maximum:", result.max_precip)



