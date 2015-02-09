from math import sqrt

# return and array of primes up to the specified max value
def PrimesArray(imax):
    primes = []
    cands = [1 for i in range(0, imax)]
    
    for i in range(2, imax ):
      if cands[i] == 0: continue
      num = i*2 
      while num < imax:
        cands[num] = 0 
        num += i
    for i in range(2, imax):
      if cands[i] == 1: primes.append(i)
    return primes

# for an input number, return an array that indicates if num is pandigital
def pandigitalArray(num, countArray = []):
  #countArray = [0 for i in range(0, 10)]
  #print countArray
  for i in range(0, len(str(num)) ):
    #print len(str(num))
    #print i
    #print str(num)[i]
    digit = int(str(num)[i])
    #print digit
    if digit == 0:
      countArray[0] = -1
      break
    prev = countArray[digit]
    countArray[digit] = prev + 1 
    if prev > 0:
      countArray[0] = -1
      break
  #print countArray
  return countArray

def pandigitalArray(num):
  countArray = [0 for i in range(0, 10)]
  #print countArray
  for i in range(0, len(str(num)) ):
    #print len(str(num))
    #print i
    #print str(num)[i]
    digit = int(str(num)[i])
    #print digit
    if digit == 0:
      countArray[0] = -1
      break
    prev = countArray[digit]
    countArray[digit] = prev + 1 
    if prev > 0:
      countArray[0] = -1
      break
  #print countArray
  return countArray

# For 'num' returns the array of proper divisors
def ProperDivisors( num ):
  ary = []
  for i in range(1, (num/2+1) ):
    if num%i == 0: ary.append(i)
  return ary
