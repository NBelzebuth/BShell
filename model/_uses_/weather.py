import requests

from model._uses_.mathplus import *
from model._uses_.ip import *

def weather(userInput):
    if is_number(list(userInput.split()[1])):
        city = str(ip.locate(userInput.split()[1]))
    else:
        city = userInput.split()[1]
    url = f"https://wttr.in/{city}"
    res = requests.get(url)
    weather = res.text.split("\n")
    for _ in range(2):
        weather.pop()

    print("\n".join(weather))

def my_weather(userInput):
    city = str(ip.locate(ip.public()))

    url = f"https://wttr.in/{city}"
    res = requests.get(url)
    weather = res.text.split("\n")
    for _ in range(2):
        weather.pop()

    print("\n".join(weather))