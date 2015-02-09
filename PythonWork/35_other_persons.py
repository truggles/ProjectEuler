def check_rotations(n, nums):
    numStr = str(n)
    for i in range(len(numStr)-1):
        numStr = numStr[1:] + numStr[0]
        if not nums[int(numStr)]:
            return False
    return True


print("Generating primes...")

nums = [1 for i in range(1000000)]
nums[0] = nums[1] = 0

for i in range(1000000):
    if nums[i]:
        for j in range(2*i, 1000000, i):
            nums[j] = 0

print("Checking rotations...")

counter = 0
for i in range(1000000):
    if nums[i] and check_rotations(i, nums):
        print(i)
        counter += 1

print(counter, "circular primes")
