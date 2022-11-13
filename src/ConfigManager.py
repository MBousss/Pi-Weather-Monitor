import json
import os
import sys

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
        return self.checkConfigValue('location')
    
    def getWeatherApiKey(self):
        return self.checkConfigValue('api_key')
    
    def getWeather(self):
        return self.checkConfigValue('weather')
    
    def checkConfigValue(self, key):
        if key not in self.config:
            sys.exit("Config value '{}' does not exists".format(key))
        
        if self.config[key] == None or len(self.config[key]) == 0:
            sys.exit("Config value '{}' is empty".format(key))
        
        return self.config[key]