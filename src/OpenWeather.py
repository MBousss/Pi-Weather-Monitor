from src.ConfigManager import ConfigManager
from urllib.request import urlopen
import json

class OpenWeather:
    def __init__(self):
        config_manager = ConfigManager()
        request_url = self.getRequestUrl(config_manager)
        self.weather_data = self.getCurrentDayData(request_url)
        self.measuring_unit = config_manager.getMeasuringUnit()
        
    def getDisplayInfo(self):
        return {
            "temp": str(self.getCurrentTemp()),
            "text": str(self.getCurrentWeatherText()),
        }
    
    def getCurrentTemp(self):
        metric = (self.measuring_unit == "metric")
        unit = metric and "C" or "F"
        return "{} {}".format(self.weather_data["current"][metric and "temp_c" or "temp_f"], unit)
     
    def getCurrentWeatherText(self):
        return self.weather_data["current"]["condition"]["text"]
    
    def getCurrentDayData(self, request_url):
        response = urlopen(request_url)
        return json.loads(response.read())
        
    def getRequestUrl(self, config_manager):
        base_url = "http://api.weatherapi.com/v1" + "/current.json"
        location = config_manager.getWeahterLocation()
        api_key = config_manager.getWeatherApiKey()
        return "{}?key={}&q={}".format(base_url, api_key, location)