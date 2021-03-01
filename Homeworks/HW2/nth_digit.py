import math
nth_digit = lambda a,b: math.floor(a/(10**(b-1)))%10# a is the num, b is the nth n_digit starting from the right