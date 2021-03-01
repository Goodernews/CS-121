def char_count(some_string):
  no_repeats = set(list(some_string)) & set(list(some_string))
  return dict((chars, some_string.count(chars)) for chars in no_repeats)