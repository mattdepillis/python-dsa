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
import re

def count_word_occurrences(word, text):
  split_string = re.split('\s|[,.?]', text.lower())

  word_occurrences = 0
  for w in split_string:
    if w == word:
      word_occurrences += 1
  
  return "{} appeared {} times in the provided text.".format(word, word_occurrences)


###################################################################################################################################
"""
  4. Write a function that returns a provided string in order of ASCII codes, from
  lowest to highest. 
"""
def reorder_by_ascii(string):
  ascii_list = []

  for char in string:
    ascii_list.append((char, ord(char)))

  sorted_list = sorted(ascii_list, key=lambda code: code[1])

  reordered_string = ''

  for pair in sorted_list:
    reordered_string += pair[0]

  return "\"{}\"".format(reordered_string)


###################################################################################################################################
"""
  5. Write an autocorrect function:
  * second capital letter of a word made lowercase.
  * duplicate word removed. DONE
  * word starting sentence should be capitalized. DONE
  * if word contains all capitals after first letter, capitalization should be reversed.
  * days of the week should be capitalized. DONE
  * handle ellipsis and periods properly. DONE
"""
sentence = """as it turned out our chance meeting with REverend
aRTHUR BElling was was to change our whole way of life, and
every sunday we'd hurry along to to St lOONY up the Cream BUn
and Jam...this was the time of our lives. Here's what I think."""

def autocorrect(string):
  autocorrected_string = ""
  days_of_week = [
    "sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"
  ]

  # split the string by sentence-ending periods -- not handling other punctuation.
  split_string = re.split('[.]', string.strip().replace('\n', ' '))
  for clause in split_string:
    # if the clause is empty, it was a period. add it to autocorrected string + continue.
    if (len(clause) == 0):
      autocorrected_string += clause.join('.')
      continue

    revised_string = ""
    split_clause = re.split('\s', clause)
  
    for i in range(len(split_clause)):
      # if first word in clause:
      if (i == 0):
        if (len(autocorrected_string) > 0):
          autocorrected_string += "."
          # if the current str len > 3 and doesn't have ellipsis at end, don't capitalize
          if ((len(autocorrected_string) > 3 and autocorrected_string[-3:] == "...")):
            # string should already contain leading space; no need to prepend.
            revised_string += split_clause[i]
        else:
          revised_string += split_clause[i].capitalize()
      else:
        if (len(revised_string) > len(split_clause[i])):
          if (revised_string[-len(split_clause[i]):].strip() == split_clause[i]):
            continue
        
        revised_string += " "

        if (re.match("^[A-Z][A-Z]", split_clause[i])):
          revised_string += split_clause[i].capitalize()
        elif (re.match("[A-Z]+", split_clause[i][1:])):
          revised_string += split_clause[i].lower().capitalize()
        elif (split_clause[i].lower() in days_of_week):
          revised_string += split_clause[i].capitalize()
        else:
          revised_string += split_clause[i]

    autocorrected_string += revised_string
        
  return autocorrected_string