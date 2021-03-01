alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
            "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
            "w", "x", "y", "z"]


import random
import math
random.seed()

#############################################################
# The following code doesn't need to be edited. It allows
# you to read a text file and store it in a single string,
# and also to write a single string to a text file. This is
# not an ideal way to work with files, but it will suffice
# for this assignment.
#############################################################

def file_to_string(filename):
    with open(filename, "r") as f:
        x = f.read()
    return x

def string_to_file(filename, s):
    with open(filename, "w") as f:
        f.write(s)



#############################################################
# A working Caesar cipher
#############################################################

simplify_string = lambda x: "".join([y.upper() for y in list(x) if y.isalpha()])

num_to_let = lambda x: letters[x%26].upper()
INSTRUCTOR
| 10/17 AT 9:04 AM
Just use alpha[x]


let_to_num = lambda x: letters.index(x.lower())
INSTRUCTOR
| 10/17 AT 9:19 AM
Just use alpha


shift_char = lambda x, y: num_to_let(let_to_num(y)-let_to_num(x))
INSTRUCTOR
| 10/17 AT 9:34 AM
This minus should be a plus.


def caesar_enc(unencoded, key):
  if str(key).isnumeric():
INSTRUCTOR
| 10/17 AT 10:15 AM
Don't handle this case

    key = int(key)
  if str(key).isalpha():
    key = letters.index(key.lower())
INSTRUCTOR
| 10/17 AT 10:20 AM
Just live in alpha

  unencoded = list(unencoded)
  encoded = []
  for char in unencoded:
    if char.isalpha():
      if char.lower()==char:
        encoded.append(letters[(letters.index(char)+key)%26])
      else:
        encoded.append(letters[(letters.index(char.lower())+key)%26].upper())
    else:
      encoded.append(char)
  return "".join(encoded)

def caesar_dec(encoded, key):
  if str(key).isnumeric():
    key = int(key)
  if str(key).isalpha():
    key = letters.index(key.lower())
  key = 26-key
  return caesar_enc(encoded, key)

#############################################################
# Breaking the Caesar cipher
#############################################################

letter_counts = lambda x: {y.upper(): x.lower().count(y) for y in letters}


normalize = lambda x : {i[0]: i[1]/ sum(x.values()) for i in x.items()}


# Uncomment the code below once the functions above are complete
# english_freqs = letter_counts(simplify_string(file_to_string("twocities_full.txt")))
# normalize(english_freqs)

# I made my own frequencies based on a cornell study
english_freqs = [14810, 2715, 4943, 7874, 21912, 4200, 3693, 10795, 13318,
                 188, 1257, 7253, 4761, 12666, 14003, 3316, 205, 10977, 11450,
                 16587, 5246, 2019, 3819, 315, 3853, 128]
english_freqs = [y/182303 for y in english_freqs]


distance = lambda x, y: sum([((x[z]-y[z])**2) for z in range(0,len(x))])**0.5


def english_ditribution_check(un_clean_string, frequencies=english_freqs):
  clean_string = "".join([x.lower() for x in list(un_clean_string) if x.isalpha()])
  prop_string = [(clean_string.count(z))/len(clean_string) for z in letters]
  k_nearest_score = sum([((frequencies[a]-prop_string[a])**2) for a in range(0,26)])**0.5
  return k_nearest_score

def break_caesar(encoded, frequencies=english_freqs):
  potential_unencodes = [caesar_dec(encoded, x) for x in range(0,26)]
  eng_distrub = [english_ditribution_check(y, frequencies) for y in potential_unencodes]
  likely_key =  eng_distrub.index(min(eng_distrub))
  return caesar_dec(encoded, likely_key)

 caesar_break = break_caesar


#############################################################
# A working Vigenere cipher
#############################################################

def vigenere_enc(unencoded, key):
  list_unencoded = list(unencoded)
  key_list = [letters.index(x) for x in list(key.lower())]
  clean_list = [letters.index(y.lower()) for y in list_unencoded if y.isalpha()]
  split_list = [clean_list[z::len(key_list)] for z in range(0,len(key_list))]

  encoded_list = [list(map(lambda b: (b + key_list[a])%26, split_list[a])) for a in range(0, len(split_list))]
  max_len_lists = max([len(j) for j in encoded_list])
  encoded_list = [i+(max_len_lists-len(i))*[None] for i in encoded_list]
  encoded_list = list(zip(*encoded_list))
  encoded_list = [item for sublist in encoded_list for item in sublist] #stackoverflow

  encoded_list = list(filter(lambda d: d!=None, encoded_list))
  encoded_list = list(map(num_to_let, encoded_list))
  encoded = []
  place_fill = 0
  for e in range (0,len(list_unencoded)):
    if list_unencoded[e].isalpha():
      if list_unencoded[e].upper()!=list_unencoded[e]:
        encoded.append(encoded_list[place_fill].lower())
      else:
        encoded.append(encoded_list[place_fill])
      place_fill+=1
    else:
      encoded.append(list_unencoded[e])
  return "".join(encoded)

def vigenere_dec(encoded, key):
  key = "".join([letters[(26-letters.index(x.lower()))%26] for x in list(key)])
  return vigenere_enc(encoded, key)


#############################################################
# Breaking the Vigenere cipher
#############################################################


split_string = lambda x, y : [list(x)[z::y] for z in range(0,y)]

def vig_break_for_length(encoded, key_length, frequencies):
  def break_caesar(encoded): # I modified it and was lazy
    potential_unencodes = [caesar_dec(encoded, x) for x in range(0,26)]
    eng_distrub = [english_ditribution_check(y, frequencies) for y in potential_unencodes]
    likely_key =  eng_distrub.index(min(eng_distrub))
    return likely_key, caesar_dec(encoded, likely_key)
  split = split_string(simplify_string(encoded).lower(), key_length)
  key = [break_caesar("".join(x))[0] for x in split]
  key = "".join(list(map(num_to_let, key)))
  decoded_message = vigenere_dec(encoded, key)
  return [key, decoded_message]

def vig_break(encoded, max_key_length, frequencies):
  list_decodes = [vigenere_break_for_length(encoded, x, frequencies)[1] for x in range (1,max_key_length+1)]
  eng_scores = [english_ditribution_check(y) for y in list_decodes]
  likely_key_len = eng_scores.index(min(eng_scores)) +1
  return vigenere_break_for_length(encoded, likely_key_len, frequencies)


#############################################################
# A working substitution cipher
#############################################################

def sub_gen_key():
  return "".join(random.sample(letters, 26)).upper()
def sub_enc(unencoded, key_letters):
  unencoded = list(unencoded)
  encoded = []
  for char in unencoded:
    if char.isalpha():
      if char.lower()==char:
        encoded.append(key_letters[(letters.index(char.lower()))].lower())
      else:
        encoded.append(key_letters[(letters.index(char.lower()))].upper())
    else:
      encoded.append(char)
  return "".join(encoded)
def sub_dec(encoded, key_letters):
  encoded = list(encoded)
  decoded = []
  for char in encoded:
    if char.isalpha():
      if char.lower()==char:
        decoded.append(letters[(key_letters.index(char.upper()))].lower())
      else:
        decoded.append(letters[(key_letters.index(char.upper()))].upper())
    else:
      decoded.append(char)
  return "".join(decoded)


#############################################################
# Breaking the substitution cipher
#############################################################

def count_trigrams(some_string):
  new_split_string = lambda x, y : [list(x)[z:z+y] for z in range(0,len(list(x))-y)]
  trigrams = new_split_string(some_string, 3)
  trigrams = list(map(tuple, trigrams))
  unique_trigrams = list(set(trigrams))
  counts = [trigrams.count(x) for x in unique_trigrams]
  return dict(zip(unique_trigrams, counts))


# Uncomment the code below once the functions above are complete
english_trigrams = count_trigrams(simplify_string(file_to_string("twocities_full.txt")))
normalize(english_trigrams)

map_log = lambda d: {i[0]: math.log(i[1]) for i in d.items()}

# Uncomment the code below once the functions above are complete
map_log(english_trigrams)

def trigram_score(s, english_trigrams):
  string_tri_counts = count_trigrams(s)

  overlap = list(set(string_tri_counts.keys()) & set(english_trigrams.keys()))
  out_dict = list(set(string_tri_counts.keys()) - set(english_trigrams.keys()))

  reduced_freq_dict = {i[0]: i[1] for i in english_trigrams if i[0] in overlap}
  #reduced_input_dict = {i[0]: i[1] for i in string_tri_counts if i[0] in overlap}
  no_match = len(out_dict)*-15

  return sum(reduced_freq_dict.values())+no_match

def sub_break(cipher, english_trigrams):
  break_key = sub_gen_key()
  best_tri_score = trigram_score(sub_dec(cipher, break_key), english_trigrams)
  for x in range(0,1000):
    t_key = list(break_key)
    let_one = random.randint(26)
    let_two = random.randint(26)
    t_key[let_one], t_key[let_two] = t_key[let_two], t_key[let_one]
    t_key = "".join(t_key)
    if trigram_score(sub_dec(cipher, t_key), english_trigrams)<best_tri_score:
      break_key = t_key
      best_tri_score = trigram_score(sub_dec(cipher, t_key), english_trigrams)
  return [break_key, sub_dec(cipher, break_key)]
