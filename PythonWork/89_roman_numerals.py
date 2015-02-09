import os
from math import floor
import re

ifile = open("89_text.txt", "r")

ary = []

for line in ifile:
  _line = line.strip()
  ary.append(_line)

sub = {            'CM' : 900,
                   'CD' : 400,
                   'XC' : 90,
                   'XL' : 40,
                   'IX' : 9,
                   'IV' : 4,}

roman_to_digit = { 'I' : 1,
                   'V' : 5,
                   'X' : 10,
                   'L' : 50,
                   'C' : 100,
                   'D' : 500,
                   'M' : 1000,}

# return an array with [0] = roman number minus subtractive terms, [1] = total digit value of the subtractive terms
def getSubs( num ):
  subTotal = 0 
  for key in sub.keys():
    repeat = True
    while repeat:
      if key in num:
        print "Key: %s in %s" % (key, num)
        num = num.replace(key, '', 1)
        print num 
        subTotal += sub[key]
      else: repeat = False
  ary = [num, subTotal]
  return ary

# Return the value of all non-subtractive numerals
def originalCount( num ):
  lineTotal = 0
  for char in num:
    lineTotal += roman_to_digit[char]
  return lineTotal   


def getLenRoman( num ):
  roman = ''
  rom = [0, 0, 0, 0, 0, 0, 0]
  subs = []
  rom[0] = int(floor(num / 1000) )
  num -= 1000 * rom[0]
  if len( str( num )) == 3 and str(num)[0] == '9':
      subs.append('CM')
      num -= 900
  rom[1] = int(floor(num / 500) ) 
  num -= 500 * rom[1]
  if len( str( num )) == 3 and str(num)[0] == '4':
    subs.append('CD')
    num -= 400
  rom[2] = int(floor(num / 100) )
  num -= 100 * rom[2]
  if len( str( num )) == 2 and str(num)[0] == '9':
    subs.append('XC')
    num -= 90
  rom[3] = int(floor(num / 50) )
  num -= 50 * rom[3]
  if len( str( num )) == 2 and str(num)[0] == '4':
    subs.append('XL')
    num -= 40
  rom[4] = int(floor(num / 10) )
  num -= 10 * rom[4]
  if len( str( num )) == 1 and str(num)[0] == '9':
    subs.append('IX')
    num -= 9
  rom[5] = int(floor(num / 5) )
  num -= 5 * rom[5]
  if len( str( num )) == 1 and str(num)[0] == '4':
    subs.append('IV')
    num -= 4
  rom[6] = int(floor(num / 1) )
  num -= 1 * rom[6]
  for i in range(0, rom[0]):
    roman = roman + 'M'
  for i in range(0, rom[1]):
    roman = roman + 'D'
  for i in range(0, rom[2]):
    roman = roman + 'C'
  for i in range(0, rom[3]):
    roman = roman + 'L'
  for i in range(0, rom[4]):
    roman = roman + 'X'
  for i in range(0, rom[5]):
    roman = roman + 'V'
  for i in range(0, rom[6]):
    roman = roman + 'I'
  print "Roman: %s" % roman
  print "Subs: %s" % subs
  return len(roman) + len(subs)*2

TotalCharsPre = 0
TotalCharsPost = 0
for line in ary:
  print "New Line: %s" % line
  TotalCharsPre += len( line )
  ary = getSubs( line )
  newNum = ary[0]
  subTotal = ary[1]
  regTotal = originalCount( newNum )
  Total = subTotal + regTotal
  print "SubTotal: %i, RegTotal: %i, Total: %i" % (subTotal, regTotal, Total)
  TotalCharsPost += getLenRoman( Total )

print "Saved chars: %i - %i = %i" % (TotalCharsPre, TotalCharsPost, (TotalCharsPre - TotalCharsPost) )
