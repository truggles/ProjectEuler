from math import factorial

total = 0
numRows = 20

for i in range(0, numRows+1): # need to include 21
    vertex = factorial(numRows)/( factorial(i)*factorial(numRows-i))
    vertSq = vertex*vertex
    total = total + vertSq

print "Total paths from a %i x %i lattice = %i" % (numRows, numRows, total)
