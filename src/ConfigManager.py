import json
import os
import sys

class ConfigManager:
    def __init__(self):
        file = open(os.path.dirname(os.path.abspath(__file__)) + "/../config.json")
        self.config = json.load(file)
        file.close()
        
    def getApi(self) -> str:
        api = self.config['weather_api']
        for key in api.keys():
            if not (os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "/../api/{}.py".format(key))) :
                sys.exit("'api/{}.py' does not exist ".format(key))
                
            if api[key] == True:
                return key;
        
        sys.exit("'weather_api' not set in config")
        
    def getMeasuringUnit(self) -> str:
        measuring_units = self.config['measuring_units']
        for key in measuring_units.keys():
            if measuring_units[key] == True:
                return key;
        
        sys.exit("'measuring_units' not set in config")
        
    def getWeahterLocation(self) -> str:
        return self.checkConfigValue('location')
    
    def getWeatherApiKey(self) -> str:
        return self.checkConfigValue('api_key')
    
    def getWeather(self) -> str:
        return self.checkConfigValue('weather')
    
    def checkConfigValue(self, key:str) -> str:
        if key not in self.config:
            sys.exit("Config value '{}' does not exists".format(key))
        
        if self.config[key] == None or len(self.config[key]) == 0:
            sys.exit("Config value '{}' is empty".format(key))
        
        return self.config[key]