#!/bin/env python3
import pyowm
import os

API_KEY = ''
CITY = ''

try:
    API_KEY = os.environ['OPENWEATHER_API_KEY']
except Exception:
    API_KEY = input('OPENWEATHER_API_KEY not exported in bash, please insert API key:')
    exit(1)

try:
    CITY = os.environ['CITY_NAME']
except Exception:
    CITY = input('CITY_NAME not exported in bash, please insert CITY_NAME: ')

owm = pyowm.OWM(API_KEY)

