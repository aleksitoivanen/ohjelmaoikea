import mysql.connector

def hae_icao(iso_country):
    sql = f"SELECT type, count(*) from airport where iso_country = '{iso_country}' group by type"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if len(tulos) >0 :
        print(f"lentokentät maassa {iso_country}:")
        for rivi in tulos:
            kentta_tyyppi = rivi[0]
            maara = rivi[1]
            print(f"{kentta_tyyppi}: {maara} kps")
    else:
        print("ei oikea maakoodi")

    return





yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='Allu8221!',
         autocommit=True
         )

kysely = input("syötä Maakoodi: ")
hae_icao(kysely)