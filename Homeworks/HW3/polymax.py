def poly2max(x_one, x_two, y_one, y_two):
  poly = lambda a,b : -1*(a**4)+(3*(a**2))-(b**4)+(5*(y**2))
  output = []
  for x in range(x_one, x_two+1):
    for y in range(y_one, y_two+1):
      output.append(poly(x,y))
  return max(output)