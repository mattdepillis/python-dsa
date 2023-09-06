"""


"""
def longest_substr_without_duplication(string):
  curr, longest_substr, encountered = "", "", set()

  for char in string:
    print(curr, char, encountered, longest_substr)
    if not char in encountered:
      curr += char
      encountered.add(char)
    else:
      if len(curr) > len(longest_substr): longest_substr = curr
      last_found_index = curr.index(char)
      curr = curr[last_found_index + 1:] + char
      encountered = set(curr)
    
  return longest_substr


if __name__ == "__main__":
  print(longest_substr_without_duplication(
    "clementisacap" # mentisac
  ))

  print(longest_substr_without_duplication(
    "abacacacaaabacaaaeaaafa" # bac
  ))