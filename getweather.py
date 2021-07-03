#!/bin/env python3
import pyowm
import os

API_KEY = ''
CITY = ''

try:
    API_KEY = os.environ['OPENWEATHER_API_KEY']
except Exception:
    API_KEY = input('OPENWEATHER_API_KEY not exported in bash, please insert API key:')

try:
    CITY = os.environ['CITY_NAME']
except Exception:
    CITY = input('CITY_NAME not exported in bash, please insert CITY_NAME: ')

owm = pyowm.OWM(API_KEY)
manager= owm.weather_manager()
location = manager.weather_at_place(CITY).weather

print('source=openweathermap, city={0}, description="{1}", temp="{2}",\
humidity="{3}"'.format(CITY,location.status,location.temperature(unit="celsius")['temp']\
,location.humidity))


