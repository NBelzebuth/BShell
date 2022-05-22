import requests
from geopy.geocoders import Nominatim

from functools import partial
import socket
import urllib, json

class ip:

    def locate(self):

        geolocator = Nominatim(user_agent="my-app")
        geocode = partial(geolocator.geocode, language="fr")

        response = requests.get(f"https://geolocation-db.com/json/{self}&position=true").json()

        geolocator = Nominatim(user_agent="my-app")
        location = geolocator.reverse(str(response["latitude"])+","+str(response['longitude']))

        return geocode(location.raw["address"]['county'])

    def local():
            return socket.gethostbyname(socket.gethostname())

    def public():
        data = json.loads(urllib.request.urlopen("http://ip.jsontest.com/").read())
        return data["ip"]