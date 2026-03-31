import requests
import json
hakusana = input("syötä paikkakunnon nimi: ")
api = "a4fe811189d9fc38e5d0b74cbbe1c5e9"
pyyntö = requests.get("http://api.openweathermap.org/data/2.5/weather",

    params = {
        "q" : hakusana,
        "appid" : api,
        "units" : "metric",
        "lang" : "fi"

    }
)

if pyyntö.status_code != 200:
    print("Virhe haettaessa säätietoja. Tarkista paikkakunnan nimi.")
else:
    print(
        "Sää paikkakunnalla",hakusana + ":",pyyntö.json()["weather"][0]["description"] + ",","lämpötila",str(pyyntö.json()["main"]["temp"]) + " °C")
