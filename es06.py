
numeri_pari = [numero for numero in range(1, 1001) if numero % 2 == 0]


numeri_dispari = [numero for numero in range(1, 1001) if numero % 2 != 0]


terza_lista = numeri_pari + numeri_dispari


print("Numeri pari:", numeri_pari)
print("Numeri dispari:", numeri_dispari)


print("Terza lista:", terza_lista)
