"""
Write a function that takes in two strings and returns the minimum number of edit operations that need to be performed on the first string to obtain the second.

3 operations:
1) insert char,
2) delete char,
3) substitute chars

TC:
SC:
"""
def levenshtein_distance(s1, s2):
  matrix = [ [x for x in range(len(s1) + 1)] for y in range(len(s2) + 1)]

  for i in range(1, len(s2) + 1):
    matrix[i][0] = matrix[i - 1][0] + 1

  for i in range(1, len(s2) + 1):

    for j in range(1, len(s1) + 1):

      # if the prev letter of the first word = the prev letter of the second word
      if s1[j - 1] == s2[i - 1]:
        matrix[i][j] = matrix[i - 1][j - 1]
      else:
        matrix[i][j] = min(
          matrix[i - 1][j],
          matrix[i][j - 1],
          matrix[i - 1][j - 1]
        ) + 1

  print(matrix)

  return matrix[-1][-1]


if __name__ == "__main__":
  # print(levenshtein_distance("cereal", "saturday"))
  # print(levenshtein_distance("biting", "mitten"))
  print(levenshtein_distance("cereal", "saturdzz"))