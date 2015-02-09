evtSet = set()

dups = 0

ifile = open('FR.txt', 'r')


#iwith open('FR.txt', 'r') as ifile:
for line in ifile:
    line = line.strip()
    info = line.split(' ')
    run = int(info[0])
    lumi = int(info[1])
    evtID = int(info[2])
    evtTuple = (run, lumi, evtID)
    if evtTuple in evtSet:
    	#print "Duplicate: %i %i %i" % (run, lumi, evtID)
    	#print "Dup not added"
    	dups = dups + 1
    	evtSet.add(evtTuple)
    	continue
    else:
    	#print "evtTuple %i %i %i is unique as was added" % (run, lumi, evtID)
    	evtSet.add(evtTuple)
ifile.close()
print "Total dups: %i" % dups
print "Total uniques: %i" % len(evtSet)

outFile = open('Out_file.txt', 'w')
i = 0
for evt in evtSet:
    print "Evt #%i: %i %i %i" % (i, evt[0], evt[1], evt[2])
    i = i + 1
    outFile.write("Evt #%i: %i %i %i\n" % (i, evt[0], evt[1], evt[2]))
outFile.close()
