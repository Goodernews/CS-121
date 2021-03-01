def down_up(n):
  if n==1:
    return [1]
  else:
    return [n]+down_up(n-1)+[n]