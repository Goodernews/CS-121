
def selectionsort(lst):
  for x in range(0, len(lst)):
    swap_on = lst[x:].index(min(lst[x:]))
    lst[swap_on+x], lst[x] = lst[x], lst[swap_on+x]