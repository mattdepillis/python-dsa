"""
Write a function that takes a string and returns its longest substring without duplicate characters in it.

TC: O(n) - loop through the string characters once
SC: O(n) - encountered could store up to n characters

NOTE: optimization over solution 1 is to track the longest substring's indices, not the substring itself. We do this by checking whether or not we need to reset the start index of the current substring, as well as the longest substr indices, at each string index. We also store a relationship between chars at their last seen indices in the encountered hash map to help.
"""
def longest_substr_without_duplication(string):
  start, longest_indices, encountered = 0, [0, 1], {}

  for i, char in enumerate(string):
    if char in encountered:
      start = max(start, encountered[char] + 1)
    if longest_indices[1] - longest_indices[0] < i + 1 - start:
      longest_indices = [start, i + 1]
    encountered[char] = i

  return string[longest_indices[0] : longest_indices[1]]


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