def down_up(x):
  a = [ b for b in range(2,x+1)]
  return a[::-1]+ [1] + a 