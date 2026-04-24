from weather import WeatherData

chattanooga = WeatherData(35.0456, -85.3097,11, 15, 2025)

chattanooga.get_temperature_data()
chattanooga.get_wind_data()
chattanooga.get_precipitation_data()

print("Avg Temp:", chattanooga.avg_temp)
print("Min Temp:", chattanooga.min_temp)
print("Max Temp:", chattanooga.max_temp)
