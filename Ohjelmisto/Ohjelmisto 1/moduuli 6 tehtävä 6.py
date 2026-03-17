import math
def laskin(halkaisija, hinta, sade, loppu):
    sade = halkaisija / 2
    loppu = 100/hinta/(math.pi*sade**2)

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
eka=laskin(halkaisija, hinta, sade,loppu)

halkaisija2 = float(input("syötä pizzan halkaisija: "))
hinta2 = float(input("Syötä pizzan hinta: "))

toka=laskin(halkaisija2, hinta2,sade,loppu)

paras=kumpi(eka,toka)

if eka<toka :
    print("ensimmäinen pizza on edullisempi, yksikköhinta:",eka, "€")
else:
    print("toinen pizza on edullisempi, yksikköhinta:" ,toka, "€")




