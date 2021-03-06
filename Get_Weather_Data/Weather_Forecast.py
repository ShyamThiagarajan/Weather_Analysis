"""Class Used to Represent parsed Weather in a standardized way.
@author
    Shyam Thiagarajan"""

class Weather_Forecast(object):
    def __init__(self, lat, lng, location, time):
        self.temperature = 0
        self.forecast = 'NO WEATHER'
        self.precipitation_chance = 0
        self.location = location
        self.LAT = lat
        self.LNG = lng
        self.day = 'Monday'
        self.time = time

    """Determines Weather Properties from XML table.
    @param self
        Weather_Forecast Object
    @param weather_table
        XML tag containing weather data
    @replaces self.forecast
    @replaces self.day
    @replaces self.temperature
    @replaces self.precipitation_chance"""
    def detWeatherProperties(self, weather_table):
        self.forecast = weather_table.weather.string
        self.day = weather_table.valid.string
        self.temperature = weather_table.temp.string
        try:
            self.precipitation_chance = weather_table.pop.string
        except Exception:
            print('Exception')
