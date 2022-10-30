Introduction
============
This package uses the Adafruit Standard LCD 16x2 screen in combination with a Raspberry Pi
to display weather info from https://www.weatherapi.com/

Requirements
------------
- https://www.weatherapi.com/ account (get api key)
- Adafruit Standard LCD 16x2 screen
- Raspberry Pi 3/4

Setup
=============

Connect the Raspberry Pi as show on  ``project_info/connections.jpg`` after this

Installing package
--------------------

    sudo apt-get upgrade
    sudo apt-get install git pip3
    pip3 install adafruit-circuitpython-charlcd

	git clone https://github.com/MBousss/Pi-Weather-Monitor.git
	cd Pi-Weather-Monitor/

Config package
--------------------

``location``: Location values https://www.weatherapi.com/docs/#apis-ip-lookup

``api_key``: https://www.weatherapi.com/my/


```json
{
    "location": "",
    "api_key": ""
}
```

Run
===

    python3 weather.py