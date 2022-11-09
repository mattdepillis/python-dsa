"""
Write a function that takes in a matrix of n * m proportions and returns an array of the matrix traversed in spiral order, starting in the matrix's top left hand corner.

TC: O(n) -- must traverse through each node. Cut off while loop if all matrix elements have been traversed
SC: O(n) -- spiral should have a size of n elements, where n = len(matrix) * len(matrix[0])
"""
def spiral_traverse(matrix):
  spiral = []
  start_row = start_col = 0
  end_row, end_col = len(matrix) - 1, len(matrix[0]) - 1

  while start_row <= end_row and start_col <= end_col:
    for col in range(start_col, end_col + 1):
      spiral.append(matrix[start_row][col])
    
    for row in range(start_row + 1, end_row + 1):
      spiral.append(matrix[row][end_col])

    for col in reversed(range(start_col, end_col)):
      if start_row == end_row:
        break
      spiral.append(matrix[end_row][col])

    for row in reversed(range(start_row + 1, end_row)):
      if start_col == end_col:
        break
      spiral.append(matrix[row][start_col])

    start_row, start_col = start_row + 1, start_col + 1
    end_row, end_col = end_row - 1, end_col - 1

  return spiral


if __name__ == "__main__":
  print(spiral_traverse([
    [1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7]
  ]))

  # print(spiral_traverse([
  #   [1],
  #   [2],
  #   [3],
  #   [4],
  #   [5],
  #   [6]
  # ]))

  # print(spiral_traverse([
  #   [1, 2, 3, 4, 5, 6, 7]
  # ]))