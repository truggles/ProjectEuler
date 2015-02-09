import os

tri = {}
ifile = open("67_triangle.txt", "r")
count = 1
for line in ifile:
  info_ = line.strip()
  info = info_.split(" ")
  #print "Info[0] %s" % info[0]
  #print "Len: %i" % len(info)
  row = 'row%s' % str(count)
  print row
  tri[row] = ()
  tri[row] = info
  for i in range(0, len(info)):
    print "Dic: %s" % tri[row][i]
    print "i: %i" % i
  count += 1


# A triangular list of lists
totRows = 100
buildRow = "row%i" % (totRows)
triangle = []
for j in range(0, totRows):
  triangle.append([])
print tri[buildRow]
triangle[(totRows-1)] = tri[buildRow]

for i in range(0, (totRows-1)):
  tmp = []
  row = totRows - 1 - i
  aboveRow = "row%s" % (row)
  nowRow = "row%s" % row
  for j in range(0, (len(tri[nowRow])) ):
    #print "J = %i" % j
    print int(tri[aboveRow][j])
    #print (row-1)
    print int(triangle[ (row) ][j])
    #print triangle[(totRows-1)][j]
    first = int(tri[aboveRow][j]) + int(triangle[row][j])
    second = int(tri[aboveRow][j]) + int(triangle[row][ (j+1) ])
    if first >= second:
      triangle[ (row-1) ].append(first)# + int(numAbove[j]))
      print "%i = %i + previous %i is bigger" % (first, int(tri[aboveRow][j]), int(triangle[row][j]))
      print "Appended = %i" % (first)# + int(numAbove[j]))
    if second > first:
      triangle[ (row-1) ].append(second)# + int(numAbove[j]))
      print "%i = %i + prev. %i is bigger" % (second, int(tri[aboveRow][j]), int(triangle[row][ (j+1) ]))
      print "Appended = %i" % (second)# + int(numAbove[j]))

print triangle[0][0]
