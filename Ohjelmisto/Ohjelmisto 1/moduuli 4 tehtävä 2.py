#Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi
# niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän.
# Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm




tuuma = float(input("syötä tuuma: "))
sentti= (tuuma*2.54)
while   tuuma >= 0 :
        print(tuuma, "tuumaa on: ", sentti, "cm")

        tuuma = float(input("syötä tuuma: "))