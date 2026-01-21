
import random

N = int(input("Kuinka monta pistettä arvotaan: "))


laskuri = 0
ympyrassa = 0

while laskuri < N:
    x = random.randint(-1000,1000) / 1000
    y = random.randint(-1000,1000) / 1000

    if x*x + y*y < 1:
        ympyrassa += 1
    laskuri += 1
pi = 4 * ympyrassa / N
print("piin likiarvo on:",pi)