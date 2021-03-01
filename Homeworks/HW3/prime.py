def is_prime(y):
    if y<1.01:
        return False
    for i in range(2,int((abs(y))**0.5+1)):
      if abs(y)%i==0:
        return False
    return True