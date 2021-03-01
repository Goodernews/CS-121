def has_duplicates (a):
  if list(set(a)&set(a))==a:
    return False
  else:
    return True