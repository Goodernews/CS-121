def flatten(some_list):
  if type(some_list)==list and len([item for item in some_list if type(item)==list])>0:
    return flatten(some_list[0]) +flatten(some_list[1:])
  else:
    if type(some_list)==list:
      return some_list
    else:
      return [some_list]