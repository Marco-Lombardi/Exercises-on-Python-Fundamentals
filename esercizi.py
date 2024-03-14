def StringDigitToList(sd):
    lista = []
    for c in sd:
     lista.append(int(c))
    return lista
print(StringDigitToList("99999"))

"""
Viene definita una lista vuota chiamata lista.
Viene eseguito un ciclo for che scorre ogni carattere nella stringa sd.
Per ogni carattere nella stringa, viene convertito in un intero usando int(c) e poi aggiunto alla lista lista usando il metodo append.
Alla fine, la funzione restituisce la lista contenente le cifre convertite in numeri interi.
Quando viene chiamata print(StringDigitToList("99999")), la funzione converte la stringa "99999" in una lista di interi [9, 9, 9, 9, 9] e la stampa a schermo.
"""

def GeneraListaDigit():
    lista = []
    for i in range(10000):
        s = str(i).zfill(4)  # zfill aggiunge zeri mancanti a sinistra per rendere la lunghezza della stringa 4
        l1 = [int(c) for c in s]
        lista.append(l1)
    return lista

print(GeneraListaDigit())

"""
Viene definita una lista vuota chiamata lista.
Viene eseguito un ciclo for che scorre i numeri da 0 a 9999 utilizzando la funzione range(10000).
Per ogni numero i, viene convertito in una stringa usando str(i) e poi viene riempito con zeri a sinistra fino a una lunghezza di 4 caratteri utilizzando il metodo zfill(4). Questo assicura che ogni numero abbia almeno 4 cifre.
Viene creata una nuova lista l1 contenente le cifre del numero convertito in stringa. Questo viene fatto utilizzando una list comprehension che itera attraverso ogni carattere della stringa e lo converte in un intero.
La lista l1 viene aggiunta alla lista principale lista.
Alla fine, la funzione restituisce la lista contenente tutte le liste di cifre generate.
Quando viene chiamata print(GeneraListaDigit()), la funzione genera una lista contenente tutte le possibili combinazioni di cifre da 0000 a 9999, ognuna rappresentata come una lista di cifre, e la stampa a schermo.
"""
