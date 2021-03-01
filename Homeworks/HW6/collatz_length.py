def collatz_length(some_int):
  if some_int==1:
    return 1
  if some_int%2==0:
    return collatz_length(some_int//2)+1
  else:
    return collatz_length(some_int*3+1)+1