from thrEuler import ProperDivisors

Max = 28123
#Max = 200
abundants = []
for j in range( 1, Max + 1):
  ary = ProperDivisors( j )
  sumProp = 0
  for i in ary:
    sumProp += i
  #print sumProp
  if sumProp > j: abundants.append( j )

#print abundants
print abundants[-1]
print "Length of abundants array: %i" % len(abundants)

#def twoByTwo( abun ):
#  ary = []
#  for j in abun:
#    for k in abun:
#      num = j + k
#      if num > Max: break
#      if num not in ary:
#        ary.append( num )
#  ary.sort()
#  print ary
#  return ary
#
#newAry = twoByTwo( abundants )
#Total = 0
#for k in range(1, Max+1):
#  if k not in newAry: Total += k
        
#print Total
def checkAbundants( i, abun ):
  print "New number: %i" % i
  for j in range(0, int(len(abun)/2) ):
    if abun[j] >= i: 
      #print "And One (J)!"
      return i
    #print "J = %i" % j
    for k in range(j, len(abun)):
      #print "K = %i" % k
      if abun[j] + abun[k] > i: 
        #print "restart"
        break
      if abun[j] + abun[k] == i:
        #print "Fail!"
        return 0
  return i

Total = 0
for num in range( 1, Max + 1): 
  Total += checkAbundants( num, abundants)

print Total
