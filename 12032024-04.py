import random

# scrivere una funzione ColoreCasuale() che torna una stringa
# causale "rosso" "giallo" "verde" "blu" "arancio" "ciano"

def ColoreCausuale():
 colori = ["rosso", "giallo", "verde", "blu", "arancio", "ciano", "rosa", "turchese", ]

 return colori [random.randint[0, len(colori)-1]]

print(ColoreCausuale())
print(ColoreCausuale())
print(ColoreCausuale())
print(ColoreCausuale())

def StringDigitToList(sd):
 lista = []
 for c in sd:
  lista.append(int(c))
 return lista 

sd="918357"
print(sd)








