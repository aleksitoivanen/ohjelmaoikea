import math
def laskin(halkaisija, hinta, sade, loppu):
    sade = halkaisija / 2
    loppu = hinta/(math.pi*sade**2)
    return loppu
def kumpi(eka, toka):
    if eka>toka:
        return toka
    else:
        return eka

sade=0
loppu=0
halkaisija = float(input("syötä pizzan halkaisija: "))
hinta = float(input("Syötä pizzan hinta: "))
laskin(halkaisija, hinta, sade, loppu)
eka=laskin(loppu)
halkaisija2 = float(input("syötä pizzan halkaisija: "))
hinta2 = float(input("Syötä pizzan hinta: "))
laskin(halkaisija, hinta, sade, loppu)
toka=laskin(loppu)
kumpi(eka, toka)
paras=kumpi(eka,toka)

print("parempi pizza: ", paras)



