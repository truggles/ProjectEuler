# Warning, this takes 5 minutes to run for 10mil

Max = 10000000


def getSquare(num):
  Len = len(str(num))
  Sum = 0
  for i in range(0, Len):
    _int = int( str( num )[i])
    Sum += _int * _int
  #print Sum
  return Sum
getSquare(89)


eightyNine = 0

for j in range(1, (Max+1)):
  #print "J ====== %i" % j
  #jSet = set()
  notInSet = True
  num = j
  while notInSet:
    newNum = getSquare(num)
    #print newNum
    if newNum == 1:
      notInSet = False
      #print "Hit 1"
    if newNum == 89:
      notInSet = False
      #print "Hit 89"
      eightyNine += 1
    num = newNum

print "Total number of 89s: %i" % eightyNine
