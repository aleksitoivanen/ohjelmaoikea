import mysql.connector

def hae_icao(ident):
    sql = f"SELECT name, municipality from airport where ident ='{ident}'"
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

kysely = input("syötä ICAO-koodii: ")
hae_icao(kysely)

