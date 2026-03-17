class Auto:

    def __init__(self, rekisteritunnus, huippunopeus, nopeus, matka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka

    def kiihdyta(self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0



#pääohjelma



auto1 = Auto("ABC-1", 142, 0, 0)
auto1.kiihdyta(30)
auto1.kiihdyta(70)
auto1.kiihdyta(50)
print(f"Auton nopeus kiihdytyksien jälkeen: {auto1.nopeus}.")
auto1.kiihdyta(-200)
print(f"Auton nopeus hätäjarrutuksen jälkeen {auto1.nopeus}. ")
print(f"auton rekisteritunnus:  {auto1.rekisteritunnus}, auton huippunopeus: {auto1.huippunopeus}, auton nykyinen nopeus: {auto1.nopeus} ja auton matka: {auto1.matka}.")