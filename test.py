from weather import WeatherData

def test_temperature_data():
    w = WeatherData(35.0456, -85.3097, 11, 15, 2025)
    w.get_temperature_data()
    assert w.avg_temp is not None
    assert w.min_temp <= w.avg_temp <= w.max_temp

def test_wind_data():
    w = WeatherData(35.0456, -85.3097, 11, 15, 2025)
    w.get_wind_data()
    assert w.avg_wind is not None

def test_precipitation_data():
    w = WeatherData(35.0456, -85.3097, 11, 15, 2025)
    w.get_precipitation_data()
    assert w.sum_precip is not None

if __name__ == "__main__":
    test_temperature_data()
    test_wind_data()
    test_precipitation_data()
    print("Tests passed")