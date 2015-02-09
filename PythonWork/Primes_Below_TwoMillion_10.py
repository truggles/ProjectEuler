from thrEuler import PrimesArray

primes = PrimesArray(200000)

total = 0
for i in range(0, len(primes)):
    total = total + primes[i]

print total


#print primes[2]
#print primes[5]
