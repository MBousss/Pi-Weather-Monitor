Introduction
============
This package uses the Adafruit Standard LCD 16x2 screen in combination with a Raspberry Pi to display weather info from supported weather APIs

Requirements
------------
- Selected account from supported APIs list
- Adafruit Standard LCD 16x2 screen + 10K ohm Potentiometer
- Raspberry Pi 3/4

Supported APIs
=============
Free tears offer enough calls per month for personal usage. (Minimum required calls per month is 3000)

- ``OpenWeatherMap``: https://openweathermap.org/

- ``WeatherApi``: https://www.weatherapi.com/

Setup
=============

Connect the Raspberry Pi as show on  ``project_info/connections.jpg`` after this

Installing package
--------------------

    sudo apt-get upgrade
    sudo apt-get install git pip3

	git clone https://github.com/MBousss/Pi-Weather-Monitor.git
	cd Pi-Weather-Monitor/

    pip3 install adafruit-circuitpython-charlcd

Config package
--------------------

Change ``config_example.json`` to ``config.json`` a update file content:

- ``location``: Enter city name
  
- ``api_key``: Enter API key of account
  
- ``weather_api``: Select API to be used [default: "OpenWeatherMap"]

- ``measuring_units``: Set measuring_unit of choice on true [default: "metric"]


```json
{
    "location": "",
    "api_key": "",
    "weather_api": {
        "OpenWeatherMap": true,
        "WeatherApi" : false
    },
    "measuring_units": {
        "metric": true,
        "imperial" : false
    }
}
```

Manuel run
===
Run the program manualy:

    python3 weather.py

Exit program by running command ``CTRL + Z``


Run on start-up
===============

! Try out ``Manuel Run`` first to make sure config is set correct  

To automatically run package on boot run this command:

	sudo python background-setup.py