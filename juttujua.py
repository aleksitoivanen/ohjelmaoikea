import mysql.connector

def hae_maa(iso_country):
    sql = f"SELECT name, continent from country where iso_country ='{iso_country}'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0 :
        for rivi in tulos:
            print(f"Maa, jonka on iso_countrykoodi on {iso_country} sijaitsee maassa {rivi [0]}. Kyseinen maa sijatsee maanosassa: {rivi[1]} .")
    return





yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='Allu8221!',
         autocommit=True
         )


hae_maa("FI")






