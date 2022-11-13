Introduction
============
This package uses the Adafruit Standard LCD 16x2 screen in combination with a Raspberry Pi to display weather info from https://www.weatherapi.com/

Requirements
------------
- https://www.weatherapi.com/ account (get api key)
- Adafruit Standard LCD 16x2 screen + 10K ohm Potentiometer
- Raspberry Pi 3/4

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

- ``location``: Location values https://www.weatherapi.com/docs/#apis-ip-lookup

- ``api_key``: https://www.weatherapi.com/my/
  
- ``measuring_units``: Set measuring_unit of choice on true [default: "metric"]


```json
{
    "location": "",
    "api_key": "",
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

Exit program by running command ``CTRL + C``


Run on start-up
===============
! Try out ``Manuel Run`` first to make sure config is set correct  

To automatically run package on boot run this command:

	sudo python background-setup.py