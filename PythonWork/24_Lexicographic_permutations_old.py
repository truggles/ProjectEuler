from math import floor

#Max = 1000000
Max = 20
finalNum = ''
#nums = [0,1,2,3,4,5,6,7,8,9]
nums = [0,1,2,3]

def Factorial( i ):
	num = 1
	if (i == 0 or i == 1):
		return num
	j = 2
	while j <= i:
		num *= j
		#print num
		j += 1
	return num

def FindFact( nums, tot ):
	cor = False
	largest = len(nums)
	factor = 0
	count = 0
	while not cor:
		if Factorial( largest ) < tot:
			factor = Factorial( largest )
			cor = True
		else:
			largest -= 1
			count += 1
	multiplier = int( floor( tot / factor ) )
	return [count, largest, factor, multiplier]

#print Factorial( 10 )
for k in range(11):
	print Factorial(k)

keepGoing = True
print nums
while keepGoing:
	print "starting again"
	if Factorial( len( nums ) ) > Max:
		finalNum += str( nums[0] )
		nums.remove( nums[0] )
		print nums
		continue
	ary = FindFact( nums, Max )
	print nums
	print ary
	finalNum += str( nums[ary[3]] )
	print "Final num: %s" % finalNum
	nums.remove( nums[ary[3]] )
	print "Max: %i" % Max
	Max -= ( ary[2]*ary[3] )
	print "New max: %i" % Max
	if Max == 0: keepGoing = False
print nums
finalNum += str( nums[0] )
print "Finished! Out number is: %s" % finalNum
