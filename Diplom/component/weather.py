import requests
from .config import weather_api

def get_weather_city(city = 'Minsk'):
    box = dict()
    url = requests.get(weather_api).json()
    box['city'] = url['name']
    box['temp'] = url['main']['temp']
    box['temp_max'] = url['main']['temp_max']
    box['temp_min'] = url['main']['temp_min']
    box['humidity'] = url['main']['humidity']
    box['pressure'] = url['main']['pressure']
    return box
