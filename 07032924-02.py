#Comprension

lista = [1, 2, 3, 4]

lista2 = [ x * x for x in lista]
print(lista2)
# Nel modo classico
lista2 = []
for x in lista:
    lista2.append(x*x)


lista = [2,3,4]
lista3 = [y for x in lista for y in range(1, x)]

print(lista3)

#funzione zip

lista_dispari = [x * 2 + 1  for x in range (0, 10)]
lista_numeri = [x for x in range (0, 10)]

print(lista_dispari)
print(lista_numeri)



