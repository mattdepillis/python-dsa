"""
Given a 2D array of potentially-unequal height and width containing integers, and a specific size representing the height and width of a potential submatrix, write a function that returns the max submatrix sum.

TC: ```O(w * h)``` - must iterate through all elements in the matrix in (w * h)-proportional manner
SC: ```O(w * h)``` - in the worst case, must store ```w * h``` number of elements in submatrix sums
"""
def max_sum_submatrix(matrix, size):
  submatrix_sums, max_sum = [], float('-inf')

  for i in range(len(matrix) - size + 1):
    submatrix_sums.append([])
    rows = range(i, i + size)

    for j in range(len(matrix[i]) - size + 1):
      s = 0
      for row in rows:
        s += sum([x for x in matrix[row][j : j + size]])
      if s > max_sum: max_sum = s
      submatrix_sums[i].append(s)

  return max_sum

if __name__ == "__main__":
  # print(max_sum_submatrix([
  #   [5, 3, -1, 5],
  #   [-7, 3, 7, 4],
  #   [12, 8, 0, 0],
  #   [1, -8, -8, 2]
  # ], 2)) # 18 ([3, 7] + [8, 0])

  # print(max_sum_submatrix([
  #   [2, 4],
  #   [5, 6],
  #   [-3, 2]
  # ], 2)) # 17

  # print(max_sum_submatrix([
  #   [1]
  # ], 1)) # 1

  # print(max_sum_submatrix([
  #   [1, 1],
  #   [1, 1]
  # ], 2)) # 4

  # print(max_sum_submatrix([
  #   [1, 1, 2, -1],
  #   [1, 1, 2, -1]
  # ], 2)) # 6

  # print(max_sum_submatrix([
  #   [2, 1, 1, 1, 1, 4, -1, 1, 1, 5],
  #   [1, -1, 1, 1, 1, 1, -1, 1, 4, 1],
  #   [-50, 12, -1, 1, 5, 1, -1, 1, 1, 1],
  #   [-52, 99, 1, -1, 1, 1, -1, 1, 1, 1],
  #   [1, -10, -287, 9, -1, 1, -1, 1, 1, 1],
  #   [1, 2, 1, 8, 1, -1, 1, 1, 1, 1],
  #   [1, 1, 1, 1, 1, 1, -1, 1, 1, 1]
  # ], 6)) # 45

  # print(max_sum_submatrix([
  #   [22, 24, -9, 23],
  #   [12, 10, -19, 35],
  #   [45, -20, -20, 99],
  #   [0, 0, 0, 0],
  #   [0, 0, 0, 0],
  #   [-100, 200, -50, 5],
  #   [5, 6, 7, 8]
  # ], 3)) # 176

  # print(max_sum_submatrix([
  #   [3, -4, 6, -5, 1],
  #   [1, -2, 8, -4, -2],
  #   [3, -8, 9, 3, 1],
  #   [-7, 3, 4, 2, 7],
  #   [-3, 7, -5, 7, -6]
  # ], 5)) # 19

  # print(max_sum_submatrix([
  #   [-1, -2, -3, -4, -5],
  #   [1, 1, 1, 1, 1],
  #   [-1, -10, -10, -4, -5],
  #   [5, 5, 5, 5, 5],
  #   [-5, -4, -3, -10, -1]
  # ], 2)) # 3

  print(max_sum_submatrix([
    [-1, -2, -3, -4, -5],
    [-5, -4, -3, -2, -1],
    [-1, -2, -3, -4, -5],
    [-5, -4, -3, -2, -1],
    [-5, -4, -3, -2, -1]
  ], 3)) # -24