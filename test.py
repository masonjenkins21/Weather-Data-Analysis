# This file runs three tests to verify that the WeatherData class correctly retrieves and processes
# weather data from the Open-Mateo API.
from weather import WeatherData

# Tests that average temperature exists and falls between min and max values
def test_temperature_data():
    w = WeatherData(35.0456, -85.3097, 11, 15, 2025)
    w.get_temperature_data()
    assert w.avg_temp is not None
    assert w.min_temp <= w.avg_temp <= w.max_temp

# Tests that average wind speed is successfully computed
def test_wind_data():
    w = WeatherData(35.0456, -85.3097, 11, 15, 2025)
    w.get_wind_data()
    assert w.avg_wind is not None

# Tests that total precipitation is successfully computed
def test_precipitation_data():
    w = WeatherData(35.0456, -85.3097, 11, 15, 2025)
    w.get_precipitation_data()
    assert w.sum_precip is not None

# Runs tests when this file is executed
if __name__ == "__main__":
    test_temperature_data()
    test_wind_data()
    test_precipitation_data()
    print("Tests passed")