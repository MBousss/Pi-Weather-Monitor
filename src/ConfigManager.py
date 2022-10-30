import json

class ConfigManager:
    def __init__(self):
        f = open("config.json")
        self.config = json.load(f)
        f.close()
        
    def getWeahterLocation(self):
        return self.config['location']
    
    def getWeatherApiKey(self):
        return self.config['api_key']
    
    def getWeather(self):
        return self.config['weather']
    