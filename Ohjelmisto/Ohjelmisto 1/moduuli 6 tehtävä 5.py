def parilliset(lista):
    uusi_lista = []
    for luku in lista:
        if luku % 2 == 0:
            uusi_lista.append(luku)
    return uusi_lista

lista = []
luku=int(input("syötä kokonaisluku:(nolla lopettaa ohjelman) "))
while luku != 0:
    lista.append(luku)
    luku = int(input("syötä kokonaisluku:(nolla lopettaa ohjelman) "))

karsittu = parilliset(lista)
print("tässä koko lista: ",lista)
print("tässä karsittu lista: ",karsittu)





