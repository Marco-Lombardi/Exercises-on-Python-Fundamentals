# generate random integer values
from random import seed
from random import randint
# seed random number generator
seed(1)
# generate some integers
for _ in range(1000000):
	value = randint(0, 10)
	print(value)