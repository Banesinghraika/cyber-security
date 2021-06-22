import requests
import os
from datetime import datetime

api_key = '8e93edf82f76d96ef1729119d18b85d6'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)

with open('project_output.txt', 'wb') as t:
    t.write(api_link.content)
