"""


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