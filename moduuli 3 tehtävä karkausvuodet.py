vuosiluku = int(input("Syötä vuosiluku: "))
if vuosiluku % 400 == 0 :
    print("vuosi on karkausvuosi")
elif vuosiluku % 100 == 0 :
    print("vuosi ei ole karkausvuosi")
elif vuosiluku % 4 == 0 :
    print("vuosiluku on karkausvuosi")



else: print("vuosiluku ei ole karkausvuosi")
