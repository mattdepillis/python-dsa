"""
Write a function that takes 2 strings and returns the longest common subsequence. Characters in the subsequence do not necessarily have to be adjacent to each other in a given string.
"""
def determine_indices(i, s1, s2):
  j, multiple = -1, False

  for c in range(len(s2)):
    if s2[c] == s1[i]:
      if j < 0: j = c
      else:
        multiple = True
        break
  
  return j, multiple

def longest_common_subsequence(s1, s2):
  subsequences, longest = {}, []

  for i in range(len(s1)):

    # verbose but quick way to find first index + is multiple or not
    j, multiple = determine_indices(i, s1, s2)

    if j >= 0:
      temp, added = {}, False
      for s in subsequences:
        temp_j = j
        if multiple and temp_j < subsequences[s][1]:
          temp_j = subsequences[s][1] + s2[subsequences[s][1]:].find(s1[i])
        if temp_j > subsequences[s][1]:
          new = s + s1[i]
          if len(new) > len(longest): longest = list(new)
          temp[new], added = [i, temp_j], True
      subsequences.update(temp)
      if not added and not s1[i] in subsequences: subsequences[s1[i]] = [i, j]
    
  return longest


if __name__ == "__main__":
  print(longest_common_subsequence("ZXVVYZW", "XKYKZPW"))
  # print(longest_common_subsequence(
  #   "8111111111111111142",
  #   "222222222822222222222222222222433333333332"
  # )) # ["8", "4", "2"]
  print(longest_common_subsequence("clement","antoine"))