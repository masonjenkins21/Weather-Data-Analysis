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


    def get_temperature_data(self):
        temps = []

        for y in range(self.year, self.year - 5, -1):
            # placeholder for API call
            temps.append(0)

        self.avg_temp = sum(temps) / len(temps)
        self.min_temp = min(temps)
        self.max_temp = max(temps)


    def get_wind_data(self):
        wind = []

        for year in range(self.year, self.year - 5, -1):
            # placeholder for API call
            wind.append(0)

        self.avg_wind = sum(wind) / len(wind)
        self.min_wind = min(wind)
        self.max_wind = max(wind)


    def get_precipitation_data(self):
        precip = []

        for year in range(self.year, self.year - 5, -1):
            # placeholder for API call
            precip.append(0)

        self.sum_precip = sum(precip)
        self.min_precip = min(precip)
        self.max_precip = max(precip)

