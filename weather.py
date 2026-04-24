import requests

class WeatherData:
    def __init__(self,
                 latitude,
                 longitude,
                 month,
                 day,
                 year):
        self.latitude = latitude
        self.longitude = longitude
        self.month = month
        self.day = day
        self.year = year

        self.avg_temp = None
        self.min_temp = None
        self.max_temp = None

        self.avg_wind = None
        self.min_wind = None
        self.max_wind = None

        self.sum_precip = None
        self.min_precip = None
        self.max_precip = None

    def get_daily_data(self, year, variable):
        date = f"{year}-{self.month:02d}-{self.day:02d}"
        response = requests.get(
            "https://archive-api.open-meteo.com/v1/archive",
            params={
                "latitude": self.latitude,
                "longitude": self.longitude,
                "start_date": date,
                "end_date": date,
                "daily": variable,
                "timezone": "auto"
            }
        )
        return response.json()

    def get_temperature_data(self):
        temps = []

        for y in range(self.year, self.year - 5, -1):
            data = self.get_daily_data(y, "temperature_2m_mean")
            temps.append(data["daily"]["temperature_2m_mean"][0])

        self.avg_temp = sum(temps) / len(temps)
        self.min_temp = min(temps)
        self.max_temp = max(temps)


    def get_wind_data(self):
        wind = []

        for y in range(self.year, self.year - 5, -1):
            data = self.get_daily_data(y, "wind_speed_10m_max")
            wind.append(data["daily"]["wind_speed_10m_max"][0])

        self.avg_wind = sum(wind) / len(wind)
        self.min_wind = min(wind)
        self.max_wind = max(wind)


    def get_precipitation_data(self):
        precip = []

        for y in range(self.year, self.year - 5, -1):
            data = self.get_daily_data(y, "precipitation_sum")
            precip.append(data["daily"]["precipitation_sum"][0])

        self.sum_precip = sum(precip)
        self.min_precip = min(precip)
        self.max_precip = max(precip)