from math import sqrt


notHighlyDivis = True
i = 1
oldTri = 0

while notHighlyDivis:
    # generate our triangular numbers from the previous one
    # do not store old ones
    tri = oldTri + i
    oldTri = tri
    #print tri
    #if tri > 30: notHighlyDivis = False
    i = i + 1

    #print "sqrt i = %i or %f" % (int(sqrt(i)), sqrt(i))

    #mx = (tri/20) + 1
    divisors = []
    for j in range(1, int(sqrt(tri)) ):
        if tri % j == 0:
            divisors.append(j)
            divisors.append( tri / j )
        if len(divisors) > 500:
            notHighlyDivis = False
            print "Triangle number %i has %i divisors." % (tri, len(divisors) )
            break
#        if not over100 and len(divisors) > 100:
#            print "Over 100"
#            over100 = True
#        if not over200 and len(divisors) > 200:
#            print "Over 200"
#            over200 = True
#        if not over300 and len(divisors) > 300:
#            print "Over 300"
#            over300 = True
#        if not over400 and len(divisors) > 400:
#            print "Over 400"
#            over400 = True
#        if not over450 and len(divisors) > 450:
#            print "Over 450"
#            over450 = True
