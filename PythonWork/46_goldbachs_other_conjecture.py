from thrEuler import PrimesArray
from math import sqrt

def goldCheck(num, primes, squares, Max):
    #print "NUM: %i" % num
    for i in range(0, len(squares) ):
      #print squares[i]
      diff = num - (2 * squares[i] )
      if diff < 0: continue
      if diff in primes:
        #print "%i = %i + ( 2 x %i )" % (num, diff, squares[i])
        return False
    print "Gold was wronge!!! %i" % (num)
    return True

Max = 1000000
sqrtMax = int(sqrt(Max))

primes = PrimesArray(Max)
#primes = [2,3,5,7]
pSet = set()
for i in range(0, len(primes) ):
  pSet.add( primes[i] )
#print pSet

squares = []
for j in range(0, sqrtMax):
  squares.append( (j+1)*(j+1) )
#print squares

complete = False
k = 1
while not complete:
  num = (k*2+1)
  if num not in pSet:
    complete = goldCheck(num, pSet, squares, Max)
  k += 1
  #if k > 500: complete = True
