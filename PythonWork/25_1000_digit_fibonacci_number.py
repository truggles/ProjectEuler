

current = 1
previous = 1
count = 2

while len(str(current)) < 1000:
  nxt = previous + current
  previous = current
  current = nxt
  count = count + 1

print count
print current
  
