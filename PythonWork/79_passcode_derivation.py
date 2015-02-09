import os

ifile = open("79_keys.txt", "r")

ary = []
for line in ifile:
  _line = line.strip()
  ary.append( [int(_line[0]), int(_line[1]), int(_line[2]) ] )

def getSets( set0, set1, set2 ):
  for i in range(0, 3):
    for j in range(0, len( ary ) ):
      if ary[j][i] != -5:
        eval("set%i.add( ary[%i][%i] )" % ( i, j, i) )

def checkNums( set0, set1, set2 ):
  for i in set0:
    if i not in set1:
      if i not in set2:
        print "Found a code digit: %i" % i
        code.append(i)
        return i

def removeNum(k, ary):
  for i in range(0, len( ary ) ):
    for j in range(0, 3):
      if ary[i][j] == k:
        #print "Match! ary[%i][%i] == %i" % (i, j, k)
        if j == 2: ary[i][j] = -5
        if j == 1:
          ary[i][j] = ary[i][(j+1)]
          ary[i][(j+1)] = -5
        if j == 0:
          ary[i][j] = ary[i][(j+1)]
          ary[i][(j+1)] = ary[i][(j+2)]
          ary[i][(j+2)] = -5
  return ary

code = []

while len(code) < 8:
  set0 = set()
  set1 = set()
  set2 = set()
  getSets( set0, set1, set2 )
  num = checkNums( set0, set1, set2 )
  ary2 = removeNum( num, ary )
  #print "Array!!!"
  #print ary2
  print "New Code:"
  print code  
