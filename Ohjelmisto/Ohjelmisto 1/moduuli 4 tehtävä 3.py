syote = input("syötä luku: ")
pienin = float(syote)
suurin = float(syote)

syote = input("syötä luku: ")

while syote != "":
    luku = float(syote)
    if luku<pienin :
        pienin = luku
    if luku>suurin :
        suurin = luku

    syote = input("syötä luku: ")

print("pienin luku:",pienin)
print("suurin luku:",suurin)

