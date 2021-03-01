import random
def statistic(i, lst):
  pivot_val = random.choice(lst)
  below = list(filter(lambda x: x<pivot_val, lst))
  if len(below)==i:
    return pivot_val
  if len(below)>i:
    return statistic(i, below)
  if len(below)<i:
    above = list(filter(lambda x: x>pivot_val, lst))
    return statistic(i-len(below)-1, above)
