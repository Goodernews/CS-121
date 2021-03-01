def word_mix(s_one, s_two):
  if s_two=="" or s_two =="":
    return [s_one + s_two]
  mix_made = [s_one+ s_two, s_two+ s_one]
  for x in range(0,len(s_one)):
    merge_segment = s_one[:x]
    left_over = s_one[x:] # added on after the fact
    mix_made+= list(map(lambda x: x+left_over, word_mix(merge_segment, s_two)))
  for x in range(0,len(s_two)):
    merge_segment = s_two[:x]
    left_over = s_two[x:] # added on after the fact
    mix_made+= list(map(lambda z: z+left_over, word_mix(s_one, merge_segment)))
  return list(set(mix_made))