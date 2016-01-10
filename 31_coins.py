
'''
0 = 2
1 = 5
2 = 10
3 = 20
4 = 50
5 = 100
'''

def getSum( list ):
    sum = 0
    #sum += list[5]*100 + list[4]*50 + list[3]*20 + list[2]*10 + list[1]*5 + list[0]*2    
    sum += list[0]*2 + list[1]*5 + list[2]*10 + list[3]*20 +list[4]*50 + list[5]*100
    #print "Sum: ",sum, " List: ", list
    return sum


def p31( amount ) :
    count = 0
    lmaster = []
    l0 = [0]*6
    lmaster.append( list(l0) )
    # 100 pence
    for n in range(0, int(amount/100)+1):
        # 50 pence
        for m in range(0, int(amount/50)+1):
            # 20 pence
            for l in range(0, int(amount/20)+1):
                # 10 pence
                for i in range(0, int(amount/10)+1):
                    # 5 pence
                    for j in range(0, int(amount/5)+1):
                        # 2 pence
                        for k in range(0, int(amount/2)+1):
                            l0[0] += 1
                            if getSum( l0 ) <= amount :
#                                print l0
                                lmaster.append( list(l0) )
                            #else : continue
                        l0[0] = 0
                        l0[1] += 1
                        if getSum( l0 ) <= amount :
#                            print l0
                            lmaster.append( list(l0) )
                    l0[1] = 0
                    l0[2] += 1
                    if getSum( l0 ) <= amount :
#                        print l0
                        lmaster.append( list(l0) )
                l0[2] = 0
                l0[3] += 1
                if getSum( l0 ) <= amount :
#                    print l0 
                    lmaster.append( list(l0) )
            l0[3] = 0
            l0[4] += 1
            if getSum( l0 ) <= amount :
#                print l0 
                lmaster.append( list(l0) )
        l0[4] = 0
        l0[5] += 1
        if getSum( l0 ) <= amount :
#            print l0 
            lmaster.append( list(l0) )
#    print lmaster

    print " ### Results ### "
    print len( lmaster )
    

p31( 200 )








