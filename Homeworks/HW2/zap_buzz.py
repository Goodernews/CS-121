import math
def zap_buzz(x):
    three_present = False
    mult_seven = False
    nth_digit = lambda a,b: math.floor(a/(10**(b)))%10# a is the num, b is the nth n_digit starting from the right
    three_present = False
    for y in range (0,int(math.floor(math.log10(x))+1)):
        if 3==nth_digit(x,y):
            three_present = True
    mult_seven = x%7==0 # checks if multiple of seven and gives boolean

    if three_present == True and mult_seven== True:
        return "zap buzz"
    if three_present == True and mult_seven== False:
        return "buzz"
    if three_present == False and mult_seven== True:
        return "zap"
    else:
        return x