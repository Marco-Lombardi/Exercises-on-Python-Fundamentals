from math import sqrt, radians 

# primo esercizio

print("hello word")

# secondo esercizio

print(sqrt(10.123**2)+(30.3456**2))

# terzo esercizio

import math

ϕ1 = radians(59.9)
λ1 = radians(10.8)
ϕ2 = radians(49.3)
λ2 = radians(-123.1)
Raggio = 6371


Distanza = 2*Raggio*math.asin(sqrt(math.sin(0.5*( ϕ2 - ϕ1 ))**2 + math.cos(ϕ1)*math.cos(ϕ2)*math.sin(0.5*(λ2-λ1))**2))

print (Distanza)

# quarto esercizio

i1 = 10
i2 = 24
s1 = "Roma"
s2 = "Milano"
f1 = 362.42
f2 = 352.76
b1 = True
b2 = False

print(i1+i2)
print(s1+s2)
print(f1+f2)
print(b1+b2)
print(i1+s1)
print(s1+i2)
print(i1+s2)
print(f2+i2)
print(i1+b1)
print(f1+b1)
print(s1+b1)
print(i1+b1)
print(b1+s1)
print(b1+f1)











