from math import sqrt

primes = [2]
#num_to_check = 600851475143
#num_divided = 600851475143
num_to_check = 600851475143

sqrt_num = int(sqrt(num_to_check))

for i in range(2,sqrt_num):
	if i%2==0: continue 
	if i%3==0: continue 
	if i%5==0: continue 
	if i%7==0: continue 
	is_prime = False
	list_len = len(primes)
	#print "list_len: %i" % list_len
	#print "i = %i" % i
	#largest_prime = primes(len(primes))
	if num_to_check / primes[list_len-1] < i:
		print "%i / %i < %i" % (num_to_check, primes[len(primes)-1], i)
		break
	for j in range(0,list_len):
		#print "j = %i" % j
		#print "prime: %i" % primes[j]
		#if i == 600851475143 and i % primes[j] != 0:
		#if i == nun_to_check and i % primes[j] != 0:
		#	print primes[j]
		if i % primes[j] == 0:
			is_prime = False
			break
		if j == list_len-1:
			is_prime = True
			primes.append(i)
			#print "%i is prime" % i
			if num_to_check % i == 0:
				print "Found prime divisor: %i" % i
				print "Largest Prime Divisor: %f" % (num_to_check / i)
				break
print "Largest Prime: %i" % primes[len(primes)-1]

#for k in range(0,len(primes)-1):
#	if num_to_check % primes[k] == 0:
#		print "Largest primes so far: %i" % primes[k]
