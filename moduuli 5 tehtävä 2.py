luvut = []
luku = input("Syötä luku: ")
while luku != "":
    luvut.append(int(luku))
    luku = input("Syötä luku: ")
luvut.sort(reverse=True)
print(luvut[:5])
