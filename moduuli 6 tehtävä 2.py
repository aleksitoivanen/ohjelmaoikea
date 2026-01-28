import random
sivu=int(input("Syötä nopan sivujen määrä: "))
def noppa():
    return random.randint(1,sivu)
silmaluku=noppa()
while silmaluku != sivu:
    silmaluku=noppa()
    print(silmaluku)