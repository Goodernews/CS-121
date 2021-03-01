def hide_errors(func):
  def fixed_func(x):
    try:
      func(x)
    except:
      return None
    return func(x)
  return fixed_func
