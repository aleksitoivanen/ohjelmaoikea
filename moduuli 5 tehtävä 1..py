import random
lukumaara = int(input("Syötä arpakuutioiden lukumäärä: "))
heitot = []
for _ in range(lukumaara) :
    heitot.append(random.randint(1,6))
print(sum(heitot))