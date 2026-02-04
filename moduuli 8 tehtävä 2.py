import mysql.connector

def hae_icao(iso_country):
    sql = f"SELECT iso_country, type from airport where airport.iso_country = country.iso_country and country.iso_country ='{ident}'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0 :
        for rivi in tulos:
            print(f"Maa, jonka on ICAO_koodi on {ident}. Lentokentän nimi on: {rivi [0]}. Kunnassa : {rivi[1]} .")
    return





yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='Allu8221!',
         autocommit=True
         )

kysely = input("syötä Maa-koodi: ")
hae_icao(kysely)