from urllib.request import urlopen
import json

class Weather:
    def __init__(self, config_manager) -> None:
        self.config_manager = config_manager
        self.weather_data = self.getCurrentDayData(self.getRequestUrl())
        
    def getDisplayInfo(self) -> dict:
        return {
            "temp": str(self.getCurrentTemp()),
            "text": str(self.getCurrentWeatherText()),
        }
    def getCurrentTemp(self) -> str:
        unit = (self.config_manager.getMeasuringUnit() == "metric") and "C" or "F"
        return "{} {}".format(self.weather_data['main']['temp'], unit)
     
    def getCurrentWeatherText(self) -> str:
        return self.weather_data['weather'][0]['main']
    
    def getCurrentDayData(self, request_url:str) -> dict:
        response = urlopen(request_url)
        return json.loads(response.read())
        
    def getRequestUrl(self) -> str:
        location = self.config_manager.getWeahterLocation()
        api_key = self.config_manager.getWeatherApiKey()
        measuring_unit = self.config_manager.getMeasuringUnit()
        return "http://api.openweathermap.org/data/2.5/weather?q={}&units={}&appid={}".format(location, measuring_unit, api_key)