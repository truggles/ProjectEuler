
first_grid = {
    1  : "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08",
    2  : "49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00",
    3  : "81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65",
    4  : "52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91",
    5  : "22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80",
    6  : "24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50",
    7  : "32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70",
    8  : "67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21",
    9  : "24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72",
    10 : "21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95",
    11 : "78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92",
    12 : "16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57",
    13 : "86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58",
    14 : "19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40",
    15 : "04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66",
    16 : "88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69",
    17 : "04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36",
    18 : "20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16",
    19 : "20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54",
    20 : "01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48",}

grid = {}

for key in first_grid.keys():
    line = first_grid[key]
    #print line
    line2 = line.strip()
    nums = line2.split(" ")
    grid[key] = (nums[0], nums[1], nums[2],nums[3], nums[4], nums[5],nums[6], nums[7], nums[8],nums[9], nums[10], nums[11],nums[12], nums[13], nums[14], nums[15],nums[16], nums[17], nums[18],nums[19])
    #print grid[key][1]

largest = 0
lrgHor = 0
lrgVert = 0
lrgDiagUp = 0
lrgDiagDown = 0

# Horizontal check
for key in grid.keys():
   for i in range(0, (len(grid[key]) - 3 )):
       prod = int(grid[key][i]) * int(grid[key][i+1]) * int(grid[key][i+2]) * int(grid[key][i+3])
       if prod > lrgHor: lrgHor = prod
       #print grid[key][i+3]

# Vertical check
for key in grid.keys():
   if key+3 > 20: break
   for j in range(0, len(grid.keys() ) ):
       prod = int(grid[key][j]) * int(grid[key+1][j]) * int(grid[key+2][j]) * int(grid[key+3][j])
       if prod > lrgVert: lrgVert = prod

# Diag Down check
for key in grid.keys():
   if key+3 > 20: break
   for k in range(0, (len(grid.keys()) - 3 ) ):
       prod = int(grid[key][k]) * int(grid[key+1][k+1]) * int(grid[key+2][k+2]) * int(grid[key+3][k+3])
       if prod > lrgDiagDown: lrgDiagDown = prod

# Diag Up check
for key in grid.keys():
   if key <= 4: continue
   for l in range(0, (len(grid.keys()) - 3 ) ):
       prod = int(grid[key][l]) * int(grid[key-1][l+1]) * int(grid[key-2][l+2]) * int(grid[key-3][l+3])
       if prod > lrgDiagUp: lrgDiagUp = prod

print "Largest Horizontal:    %i" % lrgHor
print "Largest Vertical:      %i" % lrgVert
print "Largest Diagonal Down: %i" % lrgDiagDown
print "Largest Diagonal Up:   %i" % lrgDiagUp
