def collatz(x):
    j = [0]
    while x>j[-1]:
      i = [len(j)]
      while i[-1]!=1:
        i.append([lambda y: y/2, lambda y:(y*3)+1][int(i[-1]%2)](i[-1]))
      j.append(len(i))
    return len(j)-1