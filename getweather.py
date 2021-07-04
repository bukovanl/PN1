#!/bin/env python3
import pyowm
import os

API_KEY = ''
CITY = ''

try:
    API_KEY = os.environ['OPENWEATHER_API_KEY'] # Read api key from env variable
except Exception:
    API_KEY = print('OPENWEATHER_API_KEY not exported in bash, please insert API key:')

try:
    CITY = os.environ['CITY_NAME'] # Read City from env variable
except Exception:
    CITY = print('CITY_NAME not exported in bash, please insert CITY_NAME: ')

owm = pyowm.OWM(API_KEY) # Initialize OWM
manager= owm.weather_manager()
location = manager.weather_at_place(CITY).weather # Set location for OWM

# Print results
print('source=openweathermap, city={0}, description="{1}", temp={2:.1f}, \
humidity={3}'.format(CITY,location.status,location.temperature(unit="fahrenheit")['temp']\
,location.humidity))


