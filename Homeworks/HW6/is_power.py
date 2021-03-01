def is_power(x, y):
  if x==1 or y==x:
    return True
  if y>x or y==1:
    return False
  else:
    return is_power(x/y, y)