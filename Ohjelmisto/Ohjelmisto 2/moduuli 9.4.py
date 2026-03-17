import random
from operator import truediv


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
    def kulje(self, tunnit):
        self.matka += self.nopeus * tunnit



#pääohjelma


autot = []
for i in range(1,11):
    rekkari = f"ABC-{i}"
    huippu = random.randint(100, 200)
    autot.append(Auto(rekkari, huippu, 0, 0))

KilpailuOn = True
while KilpailuOn :
    for Auto in autot:
        muutos = random.randint(-10, 15)
        Auto.kiihdyta(muutos)

        Auto.kulje(1)

        if Auto.matka >= 10000:
            KilpailuOn = False
            break



print("\nKILPAILUN TULOKSET")
print(f"{'Rekisteri':10} {'Huippu':4} {'Nopeus':6} {'Matka':5}")

for auto in autot:
    print(f"{auto.rekisteritunnus:10} {auto.huippunopeus:3} {auto.nopeus:6} {int(auto.matka):8}")
