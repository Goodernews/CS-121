def threeSum(in_lst,target):

  def twoSum(lst, sub_target):
    upper = len(lst)-1# 1 for the length, 1 for subtraction, 1 for assignment 1+1+1=3
    lower = 0 # 1 to assign
    while upper >lower: #Max of n-1 complexity
      mini_sum = lst[upper]+lst[lower] #1 to assign, 3 to find and add. 4
      if mini_sum==sub_target: #1
        return True
      if mini_sum>sub_target: #1
        upper-=1
      else: #1
        lower+=1
      #adding one on for each upper and lower complexity
    return False #1 complexity
  in_lst.sort()#n log(n)
  clean_list = in_lst[1:] #Creating clean list is 1+ (n-1)=n
  for i in in_lst[:-2]: #n-2 complexity of loop and
    if twoSum(clean_list, target-i): #sum of the length clean list for each step in n
      return True
    clean_list.pop(0) #n complexity appernatly
  return False # 1 complexity

"""
https://wiki.python.org/moin/TimeComplexity
https://www.ics.uci.edu/~brgallar/week8_2.html
Creating clean list is 1+ (n-1)

n is the length of in_list

assuming worst runtime: n*log(n)+(n-2)(1+n)+\sum_k=2^n{(k-2)(8)+1}+1
I don't want to do the summation math

summation of a range is:(n(n+1))/2= $\sum_k=1^n k$

because inner is
(n(n+1))/2= $\sum_k=1^n k$

"""
