def countsort(lst, m):
  ident_lst= [0]*m
  for x in lst:
    ident_lst[x] +=1
  lst[:] = [y for y in range (0,len(ident_lst)) for z in range(0,ident_lst[y])]