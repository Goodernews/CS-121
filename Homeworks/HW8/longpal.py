def longPalSub(s):
  check_pal = lambda x : x==x[::-1] #1 [for intialization] 1+len(x) [for each check]
  for x in range(0, len(s)-1): #2 [intialization] +sigma_j=0 ^n-1
    for y in range (0, x+1): #2 [intialization] + sigma_i=0 ^ []
      if check_pal(s[y:len(s)-x+y]): #1+checkpal complexity
        return s[y:len(s)-x+y] #1 (technially plus a slice of len palindrome)
  return s[0] #1+1[for slicing]

  """
If len 1 = 1+2+1=4
If len 2 and false = 1+2+
If len 2 and true =

general worst case scenario
1+sigma^{n-1}_{i=0}(sigma^{i+1}_{j=0}(1+1+n-i))+1+1
  """