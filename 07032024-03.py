numero = ""
while True:
    c = input("Digita 0-9,+-*/=: ")
    if len(c) > 0:
        c = c[0]
        if len(c) ==0:
         continue   
    # dovete leggere un numero sia intero, sia decimale
    # e stamparlo nella sua interezza quando viene
    # digitato un simbolo non numerico (+-*/=)
    #
    # Terminerete quando varrà la
    if c not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ","]:
        # Stampate il numero letto
        print("Il numero è: ", numero)
        break
    else:
        # costruzione del numero...
        numero = numero + c


numero = ""
virgola_count = 0

while True:
    c = input("Digita 0-9,+-*/=: ")
    
    if len(c) > 0:
        c = c[0]

    if c.isdigit() or (c == "," and virgola_count < 1):
        if c == ",":
            virgola_count += 1
        numero += c
    elif c in ["+", "-", "*", "/", "="]:
        print("Il numero è:", numero)
        break
    else:
        print("Input non valido. Riprova.")










