def add_to_target(x,y_list):
  print(y_list)
  if sum(y_list)==x or x==0:
    return True
  if len(y_list)==1:
    return False
  for z in range(0,len(y_list)):
    popping = y_list[:z]+y_list[z+1:]
    if add_to_target(x, popping)==True:
      return True
  return False