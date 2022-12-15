#!/usr/bin/env python

from src.DisplayManager import DisplayManager
from src.ConfigManager import ConfigManager
import importlib
import time

def main():
    dp = DisplayManager()
    config_manager = ConfigManager()
    
    # Import selected Weather_Api in config
    weather_api = config_manager.getApi()
    weather_manager = importlib.import_module("api.{}".format(weather_api), ".")
    
    while True:    
        ow_data = weather_manager.Weather(config_manager).getDisplayInfo()
        dp.display(ow_data)
        
        # Last updated message
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        print("Last update: {}".format(current_time))
        
        # Run every 15 minutes
        time.sleep(900)
    return 0

if __name__ == "__main__":
    main()