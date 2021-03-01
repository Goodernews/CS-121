def inverse(dict_input):
  list_new_keys = [dict_input[key] for key in dict_input]
  list_new_keys = set(list_new_keys) & set(list_new_keys)
  empty_dict = {keys:None for keys in list_new_keys}
  for elements in empty_dict:
    matching_holder = []
    for key in dict_input:
      if dict_input[key]==elements:
        matching_holder.append(key)
    empty_dict.update({elements:matching_holder})
  return empty_dict