

def GetCollatzChain(seed):
    chain = []
    chain.append(seed)
    finished = False
    num = seed
    #print seed
    while not finished:
        if num == 1:
            finished = True
            #print "All Done!"
            continue

        if num % 2 == 0: # is even
            num = num / 2
            #print num
            chain.append(num)
            continue

        if num % 2 != 0: # is odd
            num = (3 * num + 1)
            #print num
            chain.append(num)
            continue

    return chain

#newChain = GetCollatzChain(13)
#print "Length of chain: %i" % len(newChain)

longestChain = 0
seeds = []

for i in range(1, 1000000):
    #print "New seed: %i" % i
    newChain = GetCollatzChain(i)
    if len(newChain) > longestChain:
        longestChain = len(newChain)
        seeds = []
        seeds.append(i)
        continue
    if len(newChain) == longestChain:
        print "another matching length"
        seeds.append(i)
        print seeds

print "Found longest items"
print "Longest chain = %i" % longestChain
for j in range(0, len(seeds)):
    print seeds[j]



