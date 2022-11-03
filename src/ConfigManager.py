import json
import os

class ConfigManager:
    def __init__(self):
        file = open(os.path.dirname(os.path.abspath(__file__)) + "/../config.json")
        self.config = json.load(file)
        file.close()
        
    def getMeasuringUnit(self):
        measuring_units = self.config['measuring_units']
        for key in measuring_units.keys():
            if measuring_units[key] == True:
                return key;
        
    def getWeahterLocation(self):
        return self.config['location']
    
    def getWeatherApiKey(self):
        return self.config['api_key']
    
    def getWeather(self):
        return self.config['weather']