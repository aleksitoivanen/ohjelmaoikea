
def laskin():
    Litrat = (Gallona * 3.785)
    return Litrat
Gallona=float(input("Syötä gallonat: "))
Loppu=laskin()
while Gallona > 0:
    print(Loppu)
    Gallona = float(input("Syötä gallonat: "))
    Loppu=laskin()

