from thrEuler import PrimesArray

Max = 1000000
xmax = Max + 1

primes = PrimesArray(xmax)

#print primes

pSet = set()

for prime in primes:
  pSet.add(prime) 

#print pSet

count = 0

for prime in primes:
  #for i in primes:
    if len(str(prime)) < 3:
      circ = int(str(prime)[::-1])
      if circ in pSet and prime <= circ:
         print "Circular: %i and %i" % (prime, circ)
         if circ == prime: count += 1
         if circ != prime: count += 2
    if len(str(prime)) == 3:
      circ1 = int(str(prime)[1] + str(prime)[2] + str(prime)[0])
      circ2 = int(str(prime)[2] + str(prime)[0] + str(prime)[1])
      if (circ1 in pSet) and (circ2 in pSet):
        if circ1 >= prime and circ2 >= prime:
          count += 3
          print "Circular: %i, %s, %s" % (prime, circ1, circ2 )
    if len(str(prime)) == 4:
      circ1 = int(str(prime)[1] + str(prime)[2] + str(prime)[3] + str(prime)[0])
      circ2 = int(str(prime)[2] + str(prime)[3] + str(prime)[0] + str(prime)[1])
      circ3 = int(str(prime)[3] + str(prime)[0] + str(prime)[1] + str(prime)[2])
      if (circ1 in pSet) and (circ2 in pSet) and (circ3 in pSet):
        if circ1 >= prime and circ2 >= prime and circ3 >= prime:
          count += 4
          print "Circular: %i, %s, %s, %s" % (prime, circ1, circ2, circ3 )
    if len(str(prime)) == 5:
      circ1 = int(str(prime)[1] + str(prime)[2] + str(prime)[3] + str(prime)[4] + str(prime)[0])
      circ2 = int(str(prime)[2] + str(prime)[3] + str(prime)[4] + str(prime)[0] + str(prime)[1])
      circ3 = int(str(prime)[3] + str(prime)[4] + str(prime)[0] + str(prime)[1] + str(prime)[2])
      circ4 = int(str(prime)[4] + str(prime)[0] + str(prime)[1] + str(prime)[2] + str(prime)[3])
      if (circ1 in pSet) and (circ2 in pSet) and (circ3 in pSet) and (circ4 in pSet):
        if circ1 >= prime and circ2 >= prime and circ3 >= prime and circ4 >= prime:
          count += 5
          print "Circular: %i, %s, %s, %s, %s" % (prime, circ1, circ2, circ3, circ4 )
    if len(str(prime)) == 6:
      circ1 = int(str(prime)[1] + str(prime)[2] + str(prime)[3] + str(prime)[4] + str(prime)[5] + str(prime)[0])
      circ2 = int(str(prime)[2] + str(prime)[3] + str(prime)[4] + str(prime)[5] + str(prime)[0] + str(prime)[1])
      circ3 = int(str(prime)[3] + str(prime)[4] + str(prime)[5] + str(prime)[0] + str(prime)[1] + str(prime)[2])
      circ4 = int(str(prime)[4] + str(prime)[5] + str(prime)[0] + str(prime)[1] + str(prime)[2] + str(prime)[3])
      circ5 = int(str(prime)[5] + str(prime)[0] + str(prime)[1] + str(prime)[2] + str(prime)[3] + str(prime)[4])
      if (circ1 in pSet) and (circ2 in pSet) and (circ3 in pSet) and (circ4 in pSet) and (circ5 in pSet):
        if circ1 >= prime and circ2 >= prime and circ3 >= prime and circ4 >= prime and circ5 >= prime:
          count += 6
          print "Circular: %i, %s, %s, %s, %s, %s" % (prime, circ1, circ2, circ3, circ4, circ5 )
print count
