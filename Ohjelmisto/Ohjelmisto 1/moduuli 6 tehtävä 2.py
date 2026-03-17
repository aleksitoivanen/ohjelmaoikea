import random

def noppa():
    return random.randint(1,sivu)
sivu=int(input("Syötä nopan sivujen määrä: "))
silmaluku=noppa()
print(silmaluku)
while silmaluku != sivu:
    silmaluku=noppa()
    print(silmaluku)