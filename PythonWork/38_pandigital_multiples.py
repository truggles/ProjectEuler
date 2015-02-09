from thrEuler import pandigitalArray
from math import sqrt

#ary = pandigitalArray(345)
#print ary

Max = 100000000
sqrtMax = int(sqrt(Max))
largest = 0

for i in range(1, sqrtMax):
  catProd = ''
  len9 = False
  for j in range(1,10):
  #while len(catProd) < 10:
    catProd += str(i*j)
    if len(catProd) == 9:
      len9 = True
      break
    if len(catProd) > 9:
      break
  #print catProd

  if len9:
    ary = pandigitalArray( int(catProd) )
    if ary[0] == -1: continue
    if int(catProd) > largest:
      largest = int(catProd)
      print "New largest: %i from seed val %i" % (largest, i)
    else: print "Nice try: %i from seed val %i" % (largest, i)
