"""
Return the Levenshtein Distance between 2 strings.

TC: O(n * m) -- iterate through each place in the matrix
SC: O(n * m) -- matrix of size n * m
"""
def levenshtein_distance(s1, s2):
  matrix = [ [0 for _ in range(len(s1) + 1)] for _ in range(len(s2) + 1) ]

  for i in range(1, len(s2) + 1): matrix[i][0] = matrix[i - 1][0] + 1
  for j in range(1, len(s1) + 1): matrix[0][j] = matrix[0][j - 1] + 1
  
  for i in range(1, len(s2) + 1):
    for j in range(1, len(s1) + 1):
      if s1[j - 1] == s2[i - 1]: matrix[i][j] = matrix[i - 1][j - 1]
      else:
        matrix[i][j] = min(
          matrix[i - 1][j - 1],
          matrix[i][j - 1],
          matrix[i - 1][j]
        ) + 1

  return matrix[-1][-1]


if __name__ == "__main__":
  print(levenshtein_distance(
    'cereal', 'saturday'
  ))