from decimal import *
prec = 50
getcontext().prec = prec


def checkReps( numsLeft, prec,longest,lenLong ) :
    start = 100
    getcontext().prec = prec
    for i in numsLeft :
        num = Decimal(1) / Decimal(i)
        print "1/%i = %s" % (i, num)
        #print "Len num: ",len(str(num))
        len_ = len(str(num))
        num_ = str(num)
        if len_ < 10 :
            numsLeft.remove(i)
            continue
        for j in range( 2,prec/2 ) :
            if num_[start:start+j] == num_[start+j:start+2*j] :
                print "EQUAL for j:",j," : ",num_[start:start+j]," : ", num_[start+j:start+2*j]
                numsLeft.remove(i)
                if j > lenLong : 
                    print "Longer: ",i,j
                    lenLong = j
                    longest = i
                break
    
    print numsLeft
    print "Longest: ",longest
    print "Len: ",lenLong
    return (numsLeft, longest, lenLong)


longest = 0
lenLong = 0
numsLeft = []
for i in range( 2, 1000 ) :
    numsLeft.append( i )
count = 1
while len(numsLeft) > 0 :
    tup = checkReps( numsLeft, 200*count,longest,lenLong )
    numsLeft = tup[0]
    longest = tup[1]
    lenLong = tup[2]
    print "###########"
    print "After prec: ",200*count
    print numsLeft
    print "###########"
    count += 1

print "%%%%%%%"
print "Longest: ",longest
print "Len: ",lenLong





