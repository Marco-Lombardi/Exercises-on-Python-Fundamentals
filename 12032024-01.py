var = 10
nome = 0
numero = "altro"

ottimo = [1,2,3,4,5]
esempio = ("uno", nome ,var)

diz = {"nome": var, "cognome": numero, "ottimo": ottimo }

doz = [diz, 1,2,3]

for i in range(7,700,7):
 print(i)

for i in range(9,9999,2):
  print(ottimo[i %len(ottimo)])

infine = [x for x in ottimo]
infine2 = []  

a = [1,2,3]
b = [4,5,6]
c = [a,b]
d = [a,b,c]
a[2] = 0
b[1] = 1
c[0] = 999
print(d)


