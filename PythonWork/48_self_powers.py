

Sum = 0

for i in range(1, 1001):
  tmp = 1
  for j in range(1, i+1): 
    tmp = tmp * i
  
  Sum += tmp

print Sum
print str(Sum)[-10::]
