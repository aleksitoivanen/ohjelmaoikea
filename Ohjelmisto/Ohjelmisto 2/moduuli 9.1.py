class Auto:

    def __init__(self, rekisteritunnus, huippunopeus, nopeus, matka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0



nopeus = 0
matka = 0

#pääohjelma

auto1 = Auto("ABC-1", 142, 0, 0)
print(f"auton rekisteritunnus:  {auto1.rekisteritunnus}, auton huippunopeus: {auto1.huippunopeus}, auton nykyinen nopeus: {nopeus} ja auton matka: {matka}.")