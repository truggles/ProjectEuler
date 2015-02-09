numA = 999
numB = 999
isGreatest = False
isGreat = False
greatestTempNum = 0
greatestTempSt = ''
greatestNum = 0
greatestSt = ''

#while numA > numB:
for i in range(0, numA-900):
    nAtemp = numA - i
    isPalin = False

    for j in range(0, numB):
        nBtemp = numB - j
        product = nAtemp * nBtemp
        #print product
        stP = str(product)

        if len(stP) == 6 and stP[0] == stP[-1] and stP[1] == stP[-2] and stP[2] == stP[-3]:
			print "%s is a Palindrome!" % stP
			print "%s = %i x %i" % (stP, nAtemp, nBtemp)
			if greatestTempNum < product: greatestTempNum = product
			isPalin = True
			break
print "Greatest is: %i" % greatestTempNum
