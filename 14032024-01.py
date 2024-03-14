# ho stringa "123" la voglio trasformare in [1,2,3]
#definire una funzione che risolva il problema





####################################

"""fin = open("alice.txt", "r")
linee = fin.readlines()
fin.close
print(linee)"""







#dato alice.txt stampare una per riga tutte le parole

#Data una lista di stringhe eliminare dalla lista le stringhe vuote

ls = ["uno","due", "tre","","","",""," "," ", "fine"]
lista = []
for i in ls:
   if len (i) > 0:
      lista.append(i)
print(lista)      

# In questo modo elimina anche gli spazi vuoti

ls = ["uno","due", "tre","","","",""," "," ", "fine"]
lista = []
for i in ls:
   if len (i.strip()) > 0:
      lista.append(i)
print(lista)  




#contare caratteri in spazi bianchi alice.txt
#Contare quanti non spazi bianchi ci sono in alice.txt
#Contare quanti caratteri alfanumerici [a-zA-Z0-9] ci sono in alice.txt

fin = open("alice.txt", "r")
alice = fin.read()
fin.close()
alfanum = 0
for c in alice:
   if c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
      alfanum += 0

print("Caratteri alfanumerici", alfanum)      


    




