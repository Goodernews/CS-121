def is_prime(y):
    if y<1.01:
        return False
    for i in range(2,int((abs(y))**0.5+1)):
      if abs(y)%i==0:
        return False
    return True

def primes_list(a):
  x=2
  primes=[]
  while len(primes)<a:
    if is_prime(x)==True:
      primes.append(x)
    x+=1
  return primes