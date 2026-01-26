import random
def noppa():
    return random.randint(1,6)
silmaluku = noppa()
while silmaluku != 6:
    silmaluku=noppa()
    print(silmaluku)


print(silmaluku)