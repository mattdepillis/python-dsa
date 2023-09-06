"""


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