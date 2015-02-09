
primes = [2,3,5,7]

test = 7
while len(primes) < 10001:
	for j in range(0,len(primes)):
		#print "Testing: %i / %i" % (test, primes[j])
		if test % primes[j] == 0:
			#print "Not prime: %i / %i = 0" % (test, primes[j])
			break
		if j == len(primes)-1:
			#print "Added %i" % test
			primes.append(test)
	#print "It Broke!"
	test = test + 1
print "Last prime: %i" % primes[-1]
