from math import sqrt

pSet = set()

pandigit = 9
Max = 10
for z in range(3, (pandigit) ):
  Max = Max * 10
sqrtMax = int(sqrt(Max))

print Max

def countNum(num, countArray = []):
  #countArray = [0 for i in range(0, 10)]
  #print countArray
  for i in range(0, len(str(num)) ):
    #print len(str(num))
    #print i
    #print str(num)[i]
    digit = int(str(num)[i])
    #print digit
    if digit == 0:
      countArray[0] = -1
      break
    prev = countArray[digit]
    countArray[digit] = prev + 1
    if prev > 0:
      countArray[0] = -1
      break
  #print countArray
  return countArray

#countArray = [0 for i in range(0, 10)]
#ary = countNum(35069, countArray)
#print countArray
#print ary 

for j in range(1, sqrtMax ):
  if j%10 == 0: continue
  #print "J: %i" % j
  countArray = [0 for i in range(0, 10)]
  countNum(j, countArray)
  if countArray[0] == -1:
    #print "Killed at start"
    continue
  for k in range(0, (sqrtMax) ):
    if k%10 == 0: continue
    #print countArray
    multi = int( (sqrtMax) - k)
    #print "multi: %i" % multi
    prod = j * multi
    if len( str(j) + str(multi) + str(prod) ) != pandigit: 
      #print "Killed by wrong length: %i + %i + %i = len %i" % (j, multi, prod, (len( str(j) + str(multi) + str(prod) )))
      continue
    
    fstCt2 = list(countArray)
    countNum(multi, fstCt2)
    if fstCt2[0] == -1:
      #print "Killed at middle"
      #print fstCt2
      continue
    countNum(prod, fstCt2)
    if fstCt2[0] == -1:
      #print "Killed at last"
      #print fstCt2
      continue
    #print fstCt2
    print "%i x %i = %i" % (j, multi, prod)
    if prod not in pSet: pSet.add(prod)

print "Len of Pset = %i" % len(pSet)

Sum = 0
for dig in pSet:
    Sum += dig
print Sum
