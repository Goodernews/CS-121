conditional_print = lambda f : lambda x : print(x) if f(x) == True else None
is_even = lambda x: abs(x)%2==0
print_evens = conditional_print(is_even)