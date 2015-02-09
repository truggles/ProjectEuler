singles = { 0 : '',
            1 : 'One',
            2 : 'Two',
            3 : 'Three',
            4 : 'Four',
            5 : 'Five',
            6 : 'Six',
            7 : 'Seven',
            8 : 'Eight',
            9 : 'Nine',}

teens = { 10 : 'Ten',
          11 : 'Eleven',
          12 : 'Twelve',
          13 : 'Thirteen', 
          14 : 'Fourteen',
          15 : 'Fifteen',
          16 : 'Sixteen',
          17 : 'Seventeen',
          18 : 'Eighteen',
          19 : 'Nineteen',}

tens = { 0 : '',
         1 : 'Ten',
         2 : 'Twenty',
         3 : 'Thirty',
         4 : 'Forty',
         5 : 'Fifty',
         6 : 'Sixty',
         7 : 'Seventy',
         8 : 'Eighty',
         9 : 'Ninety',}

h = 'Hundred'
t = 'OneThousand'

totalSum = 0

for i in range(1, 1001):
  Sum = 0
  txt = ''
  addAnd = False
  teensTrue = False
  iStr = str(i)
  print "New Num: %i" % i
  #print iStr[-1]
  #print len(iStr)
  #print iStr
  if len(iStr) == 4:
    txt += t
    totalSum = totalSum + len(txt)
    print "i = %s" % txt
    print "Last one"
    continue
  if len(iStr) > 2:
    txt += singles[int(iStr[-3])]
    txt += h
    #print "Hundreds, for %i, added %i and %i for %s" % (i, len(h), len(singles[int(iStr[-3])]), singles[int(iStr[-3])])
  if not iStr[-2::] == '00' and len(iStr) > 2:
    #Sum = Sum + 3
    txt += 'And'
    #print "AND + 3!"
  for key in teens.keys():
    #print "Key: %i Num: %i" % (key, i)
    if int(iStr[-2::]) == int(key):
      #Sum = Sum + len(teens[key])
      txt += teens[key]
      #print "___________Teens num: %s Teens len: %i" % (teens[key], len(teens[key]))
      teensTrue = True
      continue
  if len(iStr) > 1 and not teensTrue:
    #print "Tens Num: %s Tens Len: %i" % (tens[int(iStr[-2])], len(tens[int(iStr[-2])]))
    #Sum = Sum + len(tens[int(iStr[-2])])
    txt += tens[int(iStr[-2])]
  if not teensTrue:
    #Sum = Sum + len(singles[int(iStr[-1])])
    #print "Singles Num: %s Singles Len: %i" % (singles[int(iStr[-1])], len(singles[int(iStr[-1])]))
    txt += singles[int(iStr[-1])]
  #print "Number total: %i" % Sum
  print "i = %s _____ %i long" % (txt, len(txt))
  totalSum = totalSum + len(txt)
  print "$$$__New TOTAL: %i" % totalSum
print totalSum


