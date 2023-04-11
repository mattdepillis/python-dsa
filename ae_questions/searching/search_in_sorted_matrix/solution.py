"""
Desc.

TC:
SC:
"""
def search_in_sorted_matrix(matrix, target):
  for i in reversed(range(len(matrix))):
    row_length = len(matrix[i])
    if target < matrix[i][0] or target > matrix[i][row_length - 1]: continue
    for j in range(len(matrix[i])):
      if target == matrix[i][j]: return [i, j]
  return [-1, -1]


if __name__ == "__main__":
  # print(search_in_sorted_matrix([
  #   [1, 4, 7, 12, 15, 1000],
  #   [2, 5, 19, 31, 32, 1001],
  #   [3, 8, 24, 33, 35, 1002],
  #   [40, 41, 42, 44, 45, 1003],
  #   [99, 100, 103, 106, 128, 1004]
  # ], 44))


  print(search_in_sorted_matrix([
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004]
  ], 1006))