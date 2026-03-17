def lisaa():
   icao = input("syötä lentoaseman ICAO-koodi: ")
   nimi = input("syötä lentoaseman nimi. ")
   lentoasemat[icao] = nimi
   print("Tiedot tallennettu")

def hae():
    icao = input("syötä haettava ICAO-koodi: ")
    if icao in lentoasemat:
        print(f"{icao}: {lentoasemat[icao]}")
    else:
        print("Tuntematon ICAO-koodi.")
def tulosta_valikko():
    print("\nvalitse toiminto: ")
    print("2 = etsi tietoja")
    print("1 = Lisää uusi lentoasema")
    print("9 = Lopeta")

lentoasemat = {
    "EFHK": "Helsinki_vantaa"
}

toiminto = 0

while toiminto != 9:
    tulosta_valikko()
    toiminto = int(input("Anna valinta: "))
    if toiminto == 1:
        lisaa()
    elif toiminto == 2:
        hae()
    elif toiminto == 9:
        print("Lopetit ohjelman")


    else :
        print("tuntematon toiminto")

