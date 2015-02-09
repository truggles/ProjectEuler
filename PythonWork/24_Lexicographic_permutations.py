Max = 100000
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
count = 0
num = ''

for a in nums:
  anum = str( a )
  a_nums = nums[:]
  a_nums.remove( a )
  for b in a_nums:
    bnum = anum + str( b )
    b_nums = a_nums[:]
    b_nums.remove( b )
    for c in b_nums:
      cnum = bnum + str( c )
      c_nums = b_nums[:]
      c_nums.remove( c )
      for d in c_nums:
        dnum = cnum + str( d )
        d_nums = c_nums[:]
        d_nums.remove( d )
        for e in d_nums:
          enum = dnum + str( c )
          e_nums = d_nums[:]
          e_nums.remove( e )
          for f in e_nums:
            fnum = enum + str( d )
            f_nums = e_nums[:]
            f_nums.remove( f )
            for g in f_nums:
              gnum = fnum + str( c )
              g_nums = f_nums[:]
              g_nums.remove( g )
              for h in g_nums:
                hnum = gnum + str( d )
                h_nums = g_nums[:]
                h_nums.remove( h )
                for i in h_nums:
                  inum = hnum + str( c )
                  i_nums = h_nums[:]
                  i_nums.remove( i )
                  for j in i_nums:
                    jnum = inum + str( d )
                    j_nums = i_nums[:]
                    j_nums.remove( j )
                    count += 1
                    if count == Max: print jnum
