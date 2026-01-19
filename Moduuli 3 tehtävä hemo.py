Sukupuoli = str(input("Syötä sukupuolesi: "))

if Sukupuoli == "mies" :
    hemo = float(input("Syötä hemoglobiiniarvo: "))
    if  134<hemo<195 or hemo == 134 or hemo == 195:
        print("hemoglobiiniarvosi on normaalit")
    if hemo<134 :
        print("hemoglobiiniarvosi on alhaiset")
    if hemo>195 :
        print("hemoglobiiniarvosi on korkeat")

if Sukupuoli == "nainen" :
    hemo = float(input("Syötä hemoglobiiniarvo: "))
    if 134 < hemo < 195 or hemo == 134 or hemo == 195:
        print("hemoglobiiniarvosi on normaalit")
    if hemo < 134:
        print("hemoglobiiniarvosi on alhaiset")
    if hemo > 195:
        print("hemoglobiiniarvosi on korkeat")




