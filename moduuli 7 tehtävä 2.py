nimet = set()
nimi = str(input("Syötä nimi: "))

while "" != nimi:
    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        nimet.add(nimi)
    print(nimet)
    nimi = str(input("Syötä nimi: "))


