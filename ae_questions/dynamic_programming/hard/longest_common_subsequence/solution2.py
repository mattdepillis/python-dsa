"""
Write a function that takes 2 strings and returns the longest common subsequence. Characters in the subsequence do not necessarily have to be adjacent to each other in a given string.

TC: O(n * m * min(n, m)) -- where n is the length of s1 and m is the length of s2
  - add min(n, m) because, at each index in the matrix, could store up to n or m chars, depending on which string is smaller
SC: O(n * m * min(n, m)) 
"""
def longest_common_subsequence(s1, s2):
  longest = [[[] for _ in range(len(s1) + 1)] for _ in range(len(s2) + 1)]

  for i in range(1, len(s2) + 1):
    for j in range(1, len(s1) + 1):

      """
      if the previous letters are equal, set [i][j] equal to the longest string
      at (-1, -1) in the matrix. -> builds off past values
        - e.g. at Y (s1[j=4], s2[i=2]), add Y to longest[1][3] = X -> ['X', 'Y']

      else, just set this value to the previous longest value at this row in the matrix,
      or set it equal to the longest value at this letter in the previous row in the matrix.
      """
      if s1[j - 1] == s2[i - 1]:
        longest[i][j] = longest[i - 1][j - 1] + [s2[i - 1]]
      else:
        longest[i][j] = max(longest[i][j - 1], longest[i - 1][j], key=len)
    print(longest)

  return longest[-1][-1]


if __name__ == "__main__":
  print(longest_common_subsequence("ZXVVYZW", "XKYKZPW"))
  # print(longest_common_subsequence(
  #   "8111111111111111142",
  #   "222222222822222222222222222222433333333332"
  # )) # ["8", "4", "2"]
  # print(longest_common_subsequence("clement","antoine"))