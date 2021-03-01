def filter(func, a):
  return [x for x in a if func(x)==True]