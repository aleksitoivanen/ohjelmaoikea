class Auto:

    def __init__(self, rekisteritunnus, huippunopeus, nopeus=0, matka=0):
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
    def kulje(self, tunnit):
        self.matka += self.nopeus * tunnit

class Sahkoauto(Auto):

    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus, 0, 0)
        self.akkukapasiteetti = akkukapasiteetti

class Bensaauto(Auto):

    def __init__(self, rekisteritunnus, huippunopeus, tankki):
        super().__init__(rekisteritunnus, huippunopeus, 0, 0)
        self.tankki = tankki


autot = []

autot.append(Sahkoauto("ABC-15",180, 52.5 ))
autot.append(Bensaauto("ACD-123", 165, 32.3))

autot[0].kiihdyta(60)
autot[1].kiihdyta(90)

for auto in autot:
    auto.kulje(3)

for auto in autot:
    print(f"{auto.rekisteritunnus}: {auto.matka}km {auto.nopeus}km/h")