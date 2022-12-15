from urllib.request import urlopen
import json

class Weather:
    def __init__(self, config_manager) -> None:
        self.config_manager = config_manager
        self.weather_data = self.getCurrentDayData(self.getRequestUrl())
        
    def getDisplayInfo(self) -> json:
        return {
            "temp": str(self.getCurrentTemp()),
            "text": str(self.getCurrentWeatherText()),
        }
    
    def getCurrentTemp(self) -> str:
        metric = (self.config_manager.getMeasuringUnit() == "metric")
        unit = metric and "C" or "F"
        return "{} {}".format(self.weather_data["current"][metric and "temp_c" or "temp_f"], unit)
     
    def getCurrentWeatherText(self) -> str:
        return str(self.weather_data["current"]["condition"]["text"])
    
    def getCurrentDayData(self, request_url:str) -> dict:
        response = urlopen(request_url)
        return json.loads(response.read())
        
    def getRequestUrl(self) -> str:
        location = self.config_manager.getWeahterLocation()
        api_key = self.config_manager.getWeatherApiKey()
        return "http://api.weatherapi.com/v1/current.json?key={}&q={}".format(api_key, location)