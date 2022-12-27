"""
Write a function that takes 2 strings and returns the longest common subsequence. Characters in the subsequence do not necessarily have to be adjacent to each other in a given string.
"""
def longest_common_subsequence(s1, s2):
  subsequences, longest = {}, []

  # TODO: figure out a way to search for the value in the second string in a TC-conscious manner

  for i in range(len(s1)):
    j = s2.find(s1[i])
    if j >= 0:
      temp, to_delete = {}, []
      for s in subsequences:
        if i > subsequences[s][0] and j > subsequences[s][1]:
          new = s + s1[i]
          temp[new], to_delete = [i, j], to_delete + [s]
      subsequences.update(temp)
      for key in to_delete: del subsequences[key]
      if not s1[i] in subsequences: subsequences[s1[i]] = [i, j]

  for key in subsequences.keys():
    longest = list(key) if len(key) > len(longest) else longest
    
  return longest


if __name__ == "__main__":
  print(longest_common_subsequence("ZXVVYZW", "XKYKZPW"))
  print(longest_common_subsequence(
    "8111111111111111142",
    "222222222822222222222222222222433333333332"
  )) # ["8", "4", "2"]