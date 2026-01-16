leiviska=input("Anna leiviskät: ")
naula=input("Anna naulat: ")
luoti=input("anna luodit: ")
leiviska=int(leiviska)
naula=int(naula)
luoti=int(luoti)

leiviska_g = 20 * 32 * 13.3
naula_g = 32 * 13.3
luoti_g = 13.3

gramma = ( leiviska * leiviska_g +
           naula * naula_g +
           luoti * luoti_g )
kilot = int(gramma // 1000)
loput_grammat = gramma % 1000

print("massa on", kilot, "kg ja", loput_grammat, "g")



