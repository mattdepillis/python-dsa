"""
Given a matrix of distinct integers and a target integer to find, return the indices of the target integer in the matrix. Each column and row of the matrix are sorted. If the target cannot be found, return [-1, -1].

TC: O(n + m) -- the most numbers the algorithm needs to traverse in the matrix is n + m ints
SC: O(1)
"""
def search_in_sorted_matrix(matrix, target):
  row, col = 0, len(matrix[0]) - 1

  while row < len(matrix) and col >= 0:
    if target > matrix[row][col]: row += 1
    elif target < matrix[row][col]: col -= 1
    else: return [row, col]
    
  return [-1, -1]


if __name__ == "__main__":
  print(search_in_sorted_matrix([
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004]
  ], 44))


  # print(search_in_sorted_matrix([
  #   [1, 4, 7, 12, 15, 1000],
  #   [2, 5, 19, 31, 32, 1001],
  #   [3, 8, 24, 33, 35, 1002],
  #   [40, 41, 42, 44, 45, 1003],
  #   [99, 100, 103, 106, 128, 1004]
  # ], 1006))