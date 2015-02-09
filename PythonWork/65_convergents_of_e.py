target = 100


dTemp = 0
nTemp = 0

#ary = [1,2,2,2]
# for Sqrt (2)
#ary = [1]
#for i in range(0, (target-2) ):
#  ary.append(2)
ary = [2]
tick = 2
for i in range(0, (target-1) ):
  if (i + 2) % 3 == 0:
    ary.append( tick )
    tick += 2
  else: ary.append( 1 )

print ary

for i in range(0, (len(ary)-1) ):
  #print "dTemp: %i" % dTemp 
  print "New digit: %i" % ary[-(i+1)]
  n1 = 0
  n2 = 0
  d1 = 0
  d2 = 0
  if i == 0:
    d1 = ary[-1]
    n1 = 1
  else:
    d1 = nTemp
    n1 = dTemp
  n2 = ary[-(i+2)] * d1
  d2 = d1
  print "(%i / %i) + (%i / %i)" % (n2, d2, n1, d1)
  nTemp = n1 + n2
  dTemp = d1
  print " ==>> (%i / %i)" % (nTemp, dTemp)
  if i == (len(ary)-2):
    strN = str(nTemp)
    Sum = 0
    for j in range(0, len(strN)):
      Sum += int(strN[j])
    print "Sum: %i" % Sum
  #print "dTemp: %i" % dTemp 


