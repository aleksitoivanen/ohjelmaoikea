def lista_1(numero):
    for _ in range(numero):
        lista.append(numero)
        return lista

lista = []



numero=int(input("syötä kokonaisluku: "))
while numero >= 1:
    lista_1(numero)
    numero=int(input("syötä kokonaisluku: "))

print(sum(lista))



