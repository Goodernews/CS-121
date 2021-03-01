maxSublist= lambda lst:max([lst[i:i+j] for i in range(0,len(lst)) for j in range(0,len(lst)-i)], key=sum)

"""
all cases
sigma^{n}_{i=0}(sigma^{n-i}_{j=0}(2j))
That's weird
"""