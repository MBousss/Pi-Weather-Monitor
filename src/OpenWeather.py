from src.ConfigManager import ConfigManager
from urllib.request import urlopen
import json

class OpenWeather:
    def __init__(self):
        request_url = self.getRequestUrl()
        self.weather_data = self.getCurrentDayData(request_url)
        
    def getDisplayInfo(self):
        return {
            "location": str(self.getLocationName()),
            "temp": str(self.getCurrentTemp()),
            "text": str(self.getCurrentWeatherText()),
        }
        
    def getLocationName(self):
        return self.weather_data["location"]["name"]
    
    def getCurrentTemp(self):
        return self.weather_data["current"]["temp_c"]
     
    def getCurrentWeatherText(self):
        return self.weather_data["current"]["condition"]["text"]
    
    def getCurrentDayData(self, request_url):
        response = urlopen(request_url)
        return json.loads(response.read())
        
        
    def getRequestUrl(self):
        config = ConfigManager()
        base_url = "http://api.weatherapi.com/v1" + "/current.json"
        location = config.getWeahterLocation()
        api_key = config.getWeatherApiKey()
        return "{}?key={}&q={}".format(base_url, api_key, location)