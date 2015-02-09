from math import sqrt

mx = 0
squares = []
sqSet = set()
i = 1

while mx < 1000000:
    mx = i*i
    squares.append(mx)
    sqSet.add(mx)
    i = i + 1
    
#print squares[0]
#print squares[4]

print len(squares)

for j in range(0, len(squares)):
    fst = squares[j]
    for k in range(j, len(squares)):
        sec = squares[k]
        if fst + sec in sqSet:
            if ( sqrt(fst) + sqrt(sec) + sqrt(fst + sec)) == 1000:
                print "A = %i, B = %i, C = %i" % ( sqrt(fst), sqrt(sec), sqrt(fst + sec))
            #print "A + B + C = %i" % ( sqrt(fst) + sqrt(sec) + sqrt(fst + sec))
