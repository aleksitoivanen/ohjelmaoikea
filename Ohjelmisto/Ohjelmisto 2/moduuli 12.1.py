import requests
import json


pyyntö = "https://api.chucknorris.io/jokes/random"

vastaus = requests.get("https://api.chucknorris.io/jokes/random")
if vastaus.status_code==200:
    json_vastaus = vastaus.json()
    print(json_vastaus["value"])
