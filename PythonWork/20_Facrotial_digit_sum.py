from math import factorial

fact = factorial(100)
print fact

stFact = str(fact)

Sum = 0

for i in range(0, len(stFact)):
  Sum = Sum + int(stFact[i])

print Sum
