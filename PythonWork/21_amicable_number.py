from math import sqrt

Sum = 0
storage = {}
Min = 1
Max = 10000

for i in range(Min, Max):
  divisorTotal = 0
  for j in range(1, int( sqrt(i) + 1) ):
    k_ = i%j
    k = (i/j)
    if k_ == 0:
      divisorTotal += (j + k )
      #print "%i is divided by %i and %i" % (i, j, k)
  divisorTotal -= i
  #print divisorTotal
  storage[i] = divisorTotal
print storage[220]
print storage[284]

for l in range(Min, Max):
  val = storage[l]
  #print val
  #print l
  if val >= Max: continue
  if storage[val] == l and val != l:
    print "Amicable numbers! %i and %i" % (l, val)
    Sum += l
  
print "Greand Total: %i" % Sum
