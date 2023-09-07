"""
Write a function that takes a string and returns its longest substring without duplicate characters in it.

TC: O(n) - loop through the string characters once
SC: O(n) - curr, prev_longest, and encountered could store up to n characters each

NOTE: this could be optimized by tracking indices, rather than storing the current substring and prev longest in strings. Additionally, resetting ```encountered``` every time there's a duplicate char is inefficient.
"""
def longest_substr_without_duplication(string):
  curr, prev_longest, encountered = "", "", set()

  for char in string:
    if char in encountered:
      if len(curr) > len(prev_longest): prev_longest = curr
      last_found_index = curr.index(char)
      curr = curr[last_found_index + 1:]
      encountered = set(curr)

    curr += char
    encountered.add(char)
    
  return curr if len(curr) > len(prev_longest) else prev_longest


if __name__ == "__main__":
  # print(longest_substr_without_duplication(
  #   "clementisacap" # mentisac
  # ))

  # print(longest_substr_without_duplication(
  #   "abacacacaaabacaaaeaaafa" # bac
  # ))

  print(longest_substr_without_duplication(
    "abcbde" # cbde
  ))