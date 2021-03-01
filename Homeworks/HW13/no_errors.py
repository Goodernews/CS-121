def no_errors(func, x):
  for i in range(0,x+1):
    try:
      func(i)
    except:
      return False
  return True