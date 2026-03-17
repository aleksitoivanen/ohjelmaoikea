from selectors import SelectSelector

Mitta = float(input(" Anna kuhan pituus: "))
if  Mitta>=37 :
    print("Voit nostaa kuhan!")

if Mitta<37 :
    print("et voi nostaa kuhaa, koska kuha on", str(37-Mitta)+ "centtimetriä liian lyhyt")


