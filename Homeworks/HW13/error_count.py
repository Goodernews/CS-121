def countsort(lst, m):
  try:
    assert type(lst)==type([]), "Please give a list for the first input"
    assert type(m)==type(3), "Please give an integer for the second input"
    assert max(lst)<m, "Contains elements greater than or including m1"
    assert min(lst)>0, "Smallest element in list is less than 0"
    assert m>0, "M must be greater than zero"
    assert [type(i) for i in lst ]==[type(2)]*len(lst), "List contains non integer values"

    ident_lst= [0]*m
    for x in lst:
      ident_lst[x] +=1
    lst[:] = [y for y in range (0,len(ident_lst)) for z in range(0,ident_lst[y])]
  except:
      raise AssertionError