class Julkaisu :

    julkaistujen_lukumaara = 0
    def __init__(self, nimi):
        Julkaisu.julkaistujen_lukumaara = Julkaisu.julkaistujen_lukumaara +1
        self.julkaisunumero = Julkaisu.julkaistujen_lukumaara
        self.nimi=nimi


    def tulosta(self):
        print(f"{self.julkaisunumero}, {self.nimi}")
class Kirja(Julkaisu) :

    def __init__(self, nimi, kirjoittaja, sivumaara, ):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta(self):
        super().tulosta()
        print(f"{self.kirjoittaja}, {self.sivumaara}")

class Lehti(Julkaisu)  :

    def __init__(self,nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta(self):
        super().tulosta()
        print(f"{self.paatoimittaja}")

julkaisut = []
julkaisut.append(Kirja("hytti n:o 6", "Rosa Liksom", 200))
julkaisut.append(Lehti("Aku Ankka", "Aki Hyyppä"))

for julkaisu in julkaisut:
    julkaisu.tulosta()