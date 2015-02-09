row1 = "75"
row2 = "95 64"
row3 = "17 47 82"
row4 = "18 35 87 10"
row5 = "20 04 82 47 65"
row6 = "19 01 23 75 03 34"
row7 = "88 02 77 73 07 63 67"
row8 = "99 65 04 28 06 16 70 92"
row9 = "41 41 26 56 83 40 80 70 33"
row10 = "41 48 72 33 47 32 37 16 94 29"
row11 = "53 71 44 65 25 43 91 52 97 51 14"
row12 = "70 11 33 28 77 73 17 78 39 68 17 57"
row13 = "91 71 52 38 17 14 91 43 58 50 27 29 48"
row14 = "63 66 04 68 89 53 67 30 73 16 69 87 40 31"
row15 = "04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"

# A triangular list of lists
triangle = [ [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

#row1 = "3"
#row2 = "7 4"
#row3 = "2 4 6"
#row4 = "8 5 9 3"
#
##triangle = [ [],[],[],[]]

bottom = row15.split(' ')
for k in range(0, len(bottom)):
  triangle[14].append(bottom[k])
  print triangle[14][k]

for i in range(0, 14):
  tmp = []
  row = 15 - i
  aboveRow = eval("row%s" % (row-1))
  nowRow = eval("row%s" % row)
  #print nowRow
  numNow = nowRow.split(" ")
  numAbove = aboveRow.split(" ")
  #print "numNow: %s" % numNow[0]
  #print "numAbove: %s" % numAbove[0]
  print "____row: %i" % (row-1)
  #triangle[ (row-2) ].append(numNow[0])
  #print triangle[ (row-2) ][0]
  #print "Len nowRow = %i" % len(nowRow)
  for j in range(0, (len(numNow) - 1) ):
    #print "J = %i" % j
    #print "numNow: %s" % numNow[j]
    #print "numAbove: %s" % numAbove[j]
    first = int(numAbove[j]) + int(triangle[ (row-1) ][j])
    second = int(numAbove[j]) + int(triangle[ (row-1) ][ (j+1) ])
    if first >= second:
      triangle[ (row-2) ].append(first)# + int(numAbove[j]))
      print "%i = %i + previous %i is bigger" % (first, int(numAbove[j]), int(triangle[ (row-1) ][j]))
      print "Appended = %i" % (first)# + int(numAbove[j]))
    if second > first:
      triangle[ (row-2) ].append(second)# + int(numAbove[j]))
      print "%i = %i + prev. %i is bigger" % (second, int(numAbove[j]), int(triangle[ (row-1) ][ (j+1) ]))
      print "Appended = %i" % (second)# + int(numAbove[j]))

print triangle[0][0]

 
