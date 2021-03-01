import math
def numpal(x):
    num_digits = math.ceil(math.log10(x))
    n_digit = lambda a,b: math.floor(a/(10**b))%10# a is the num, b is the nth n_digit starting from the right
    flipped = 0
    if x==1:
      num_digits=1
    for i in range (0,num_digits):
      holder = (n_digit(x,i))
      flipped += holder*(10**(num_digits-i-1))
    return x==flipped
