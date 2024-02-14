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








