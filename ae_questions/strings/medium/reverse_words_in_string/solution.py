"""
Write a function that takes a string of words (including special characters, like . and !, attached to given words) separated by whitespace(s) and returns that string of words, reversed.

TC: O(n) proportional - 2 O(n) operations = 1. split words, 2. loop through each item in the reversed array and add it + maybe space to string
SC: O(n) proportional - could store up to n words in array (if letters) and must return a string of the same length as original
"""
def reverse_words_in_string(words):
  w, reverse = words.split(' '), ''
  for i, substr in enumerate(reversed(w)):
    reverse += substr+' ' if i < len(w) - 1 else substr
  return reverse


if __name__ == "__main__":
  print(reverse_words_in_string("this this words this this this words this"))
  print(reverse_words_in_string("..H,, hello 678"))
  print(reverse_words_in_string("this      string     has a     lot of   whitespace"))