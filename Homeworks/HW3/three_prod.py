def three_prod(x):
  def factor(y):
    factored = []
    for i in range(1,int(y//2+1)):
      if y%i==0:
        factored.append(i)
    return factored

  factors = factor(x) #all factors of intial number
  prods = []
  for j in factors:
    for k in factors:
      for l in factors:
        if j*k*l==x:
          holder_prod = [j,k,l]
          holder_prod.sort()
          if holder_prod not in prods:
            prods.append(holder_prod)
  return len(prods)+1