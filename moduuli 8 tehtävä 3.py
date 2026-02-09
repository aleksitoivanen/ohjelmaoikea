import mysql.connector
from geopy.distance import distance

def hae_koordinaatit(icao):
    sql = f"select latitude_deg, longitude_deg from airport where ident = '{icao}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()

    if tulos:
        return tulos[0], tulos[1]

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='root',
         password='Allu8221!',
         autocommit=True
)

icao1 = input("Anna ensimmäinen ICAO-koodi: ").upper()
icao2 = input("Anna toinen ICAO_koodi: ").upper()

koordi1 = hae_koordinaatit(icao1)
koordi2 = hae_koordinaatit(icao2)

if koordi1 is None:
    print(f"ICAO-koodia {icao1} ei löytynyt.")
elif koordi2 is None:
    print(f"ICAO-koodia {icao2} ei löytynyt.")
else:

    etaisyys = distance(koordi1, koordi2).km
print(f"Lentokenttien {icao1} ja {icao2} välinen etäisyys on {etaisyys: .2f} km.")



