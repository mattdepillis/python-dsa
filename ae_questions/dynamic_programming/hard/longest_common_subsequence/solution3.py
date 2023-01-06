"""
Write a function that takes 2 strings and returns the longest common subsequence. Characters in the subsequence do not necessarily have to be adjacent to each other in a given string.

TC: O(n * m) -- where n is the length of s1 and m is the length of s2
SC: O(n * m)
"""
def longest_common_subsequence(s1, s2):
  longest = [ [[None, 0, None, None] for _ in range(len(s1) + 1)] for _ in range(len(s2) + 1) ]

  
  
  return longest


if __name__ == "__main__":
  # print(longest_common_subsequence("ZXVVYZW", "XKYKZPW"))
  # print(longest_common_subsequence(
  #   "8111111111111111142",
  #   "222222222822222222222222222222433333333332"
  # )) # ["8", "4", "2"]
  print(longest_common_subsequence("clement","antoine"))