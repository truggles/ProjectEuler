sum = 2
previous = 1
current = 2
i = 0
while i <= 4000000:
	i = previous + current
	previous = current
	current = i
	if i%2==0:
		sum = sum + i
print sum
