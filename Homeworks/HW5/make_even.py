def make_even(a):
  a[:] = [ [lambda y: y+0, lambda y:y-1][int(i%2)](i) for i in a]