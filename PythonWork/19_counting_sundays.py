Day1_1900 = 1
firstDay = -1
endYear = 2000 + 1
startYear = 1901
sundays = set()

leapYears = set()

firstDay = 365 % 7 + Day1_1900
print firstDay

for i in range(startYear, endYear):
  if i%4 == 0:
    leapYears.add(i)
    #print i

SundayCount = 0
#totalDays = (endYear - startYear) * 365 + len(leapYears)
totalDays = firstDay
print totalDays

for year in range(startYear, endYear):
  print "Year = %i" % year
  #Jan
  if totalDays % 7 == 0:
    SundayCount += 1
    print "%i Jan" % year
  totalDays += 31
  #Feb
  if totalDays % 7 == 0:
    SundayCount +=1
    print "%i Feb" % year
  if year in leapYears: totalDays += 29
  if year not in leapYears: totalDays += 28
  #March
  if totalDays % 7 == 0:
    SundayCount += 1
    print "%i March" % year
  totalDays += 31
  #April
  if totalDays % 7 == 0:
    SundayCount += 1
    print "%i April" % year
  totalDays += 30
  #May
  if totalDays % 7 == 0:
    SundayCount += 1
    print "%i May" % year
  totalDays += 31
  #June
  if totalDays % 7 == 0:
    SundayCount += 1
    print "%i June" % year
  totalDays += 30
  #July
  if totalDays % 7 == 0:
    SundayCount += 1
    print "%i July" % year
  totalDays += 31
  #Aug
  if totalDays % 7 == 0:
    SundayCount += 1
    print "%i Aug" % year
  totalDays += 31
  #Sept
  if totalDays % 7 == 0:
    SundayCount += 1
    print "%i Sept" % year
  totalDays += 30
  #Oct
  if totalDays % 7 == 0:
    SundayCount += 1
    print "%i Oct" % year
  totalDays += 31
  #Nov
  if totalDays % 7 == 0:
    SundayCount += 1
    print "%i Nov" % year
  totalDays += 30
  #Dec
  if totalDays % 7 == 0:
    SundayCount += 1
    print "%i Dec" % year
  totalDays += 31
  print "Days left: %i" % totalDays

print SundayCount
