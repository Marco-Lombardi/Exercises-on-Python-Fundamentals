import random

lunghezza_lista = 100

numeri_casuali = [random.randint(1, 10) for _ in range(lunghezza_lista)]

print("Lista di numeri casuali:", numeri_casuali)

somma_numeri = sum(numeri_casuali)

print("Somma di tutti i numeri nella lista:", somma_numeri)
