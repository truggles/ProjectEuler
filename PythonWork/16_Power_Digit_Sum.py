from math import *

prod = 1

for i in range(0, 1000):
  prod = prod*2

print prod

Sum = 0
stProd = str(prod)

for j in range(0, len(stProd)):
  Sum = Sum + int(stProd[j])

print Sum
