"""
Write a function that takes in a string of lowercase English letters and returns the index of the string's first non-repeating character. If there is no non-repeating character, return -1.
"""
def non_repeating_character(string):
  chars = {}
  for char in string:
    if char not in chars:
      chars[char] = 0
    chars[char] += 1

  for key, value in chars.items():
    if value == 1:
      return string.index(key)

  return -1


if __name__ == "__main__":
  print(non_repeating_character('hheello'))