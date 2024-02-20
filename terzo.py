
r1 = int(input("Inserire il raggio della base superiore della botte: "))
r2 = int(input("Inserire il raggio del cerchio massimo: "))
r3 = int(input("inserire il raggio della base inferiore: "))
h = int(input("Inserire l'altezza della botte: "))
p = 3.1415
S1 = p*(r1**2)
S1 = p*(r2**2)
S1 = p*(r3**2)
V = 1/6*h*(S1+(4*S2)+S3)
Litri = V/1000
print(litri)