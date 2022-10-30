#!/usr/bin/env python

from src.OpenWeather import OpenWeather
from src.DisplayManager import DisplayManager
import time

def main():
    while True:
        ow = OpenWeather()
        ow_data = ow.getDisplayInfo()
        
        dp = DisplayManager()
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