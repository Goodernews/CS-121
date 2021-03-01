def iterate(func, num_iter):
  def completed(x):
    output = x
    for y in range(num_iter):
      output = func(output)
    return output
  return completed