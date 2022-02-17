"""
  1. Count how many of each vowel is in a given text string.
  -- print the frequency of each vowel in a formatted string, in order of decreasing frequency.
"""
def count_vowels(string):
  vowel_dict = {}
  vowels = ["a", "e", "i", "o", "u"]

  for vowel in vowels:
    count = 0
    for char in string.replace(" ", ""):
      if char == vowel: count += 1
    vowel_dict[vowel] = count

  sorted_by_freq = sorted(
    vowel_dict.items(),
    key=lambda vowel: vowel[1],
    reverse=True
  )
  reply = "Here is a ranking of vowel frequency in the provided string:"
  for comb in sorted_by_freq:
    reply += "\n{}: {}".format(comb[0], comb[1])

  return reply


###################################################################################################################################
"""
  2. Scan the text and print out all characters in between the brackets.
  -- note: not using the "re" library to make this harder
"""
TEXT = """
And sending tinted postcards of places they don't realise they haven ' t even visited to ' All at nu[m]ber 22, weather w[on]derful,
our room is marked with an 'X'. Wish you were here. Food very greasy but we ' ve found a charming li[t]tle local place hidden
awa[y ]in the back streets where they serve Watney ' s Red Barrel and cheese and onion cris[p]s and the accordionist pla[y]s 
"Maybe i[t]'s because I'm a Londoner"' and spending four days on the tarmac at Luton airport on a five-day package tour wit[h] 
n[o]thing to eat but dried Watney's sa[n]dwiches..."""

def find_bracketed_chars(text):
  bracketed_strings = []

  # take the array from index 1-on, because the first item is the string preceding the first "[" (has no enclosing "]")
  for string in text.split('[')[1:]:
    bracketed_strings.append(string.split(']')[0])

  return bracketed_strings


###################################################################################################################################
"""
  3. Count how many times the standalone word "wood" appears in the following text.
"""
TEXT_2 = """How much wood would a woodchuck chuck If a woodchuck could chuck wood?
He would chuck , he would , as much as he could , And chuck as much as a woodchuck would
If a woodchuck could chuck wood."""

def count_word_occurrences(text):
  return text

print(count_word_occurrences(TEXT_2))
