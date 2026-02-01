
def laskin(Litrat):
    Litrat = (Gallona * 3.785)
    return Litrat
Litrat = 0
Gallona=float(input("Syötä gallonat: "))
Litrat=laskin(Litrat)
while Gallona > 0:
    print(Litrat)
    Gallona = float(input("Syötä gallonat: "))
    Litrat=laskin(Litrat)

