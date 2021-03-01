def twoSum(lst, target):
  lst.sort() #n log(n)
  upper = len(lst)-1# 1 for the length, 1 for subtraction, 1 for assignment 1+1+1=3
  lower = 0 # 1 to assign
  while upper >lower: #Max of n-1 complexity
    mini_sum = lst[upper]+lst[lower] #1 to assign, 3 to find and add. 4
    if mini_sum==target: #1
      return True
    if mini_sum>target: #1
      upper-=1
    else: #1
      lower+=1
    #adding one on for each upper and lower complexity
  return False #1 complexity

  """

I failed at binary search
Worst or false: n*log(n)+(n-2)(4+1+1+1+1)+1=
Best: n*log(n)+6
Average: No idea

  """