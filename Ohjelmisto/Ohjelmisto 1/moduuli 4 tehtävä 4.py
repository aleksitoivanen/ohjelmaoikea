import random

luku=int(input("Arvaa luku 1-10: "))
arpa = random.randint(1,10)
while luku != arpa:
    if luku < arpa :
        print("liian pieni arvaus")
    elif luku > arpa :
        print("liian suuri arvaus")

    luku=int(input("Arvaa luku 1-10: "))
print("Oikein!")

