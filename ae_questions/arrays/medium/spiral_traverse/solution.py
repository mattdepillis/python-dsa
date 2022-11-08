"""
Write a function that takes in a matrix of n * m proportions and returns an array of the matrix traversed in spiral order, starting in the matrix's top left hand corner.
"""
def spiral_traverse(matrix):
  spiral = []
  iterations = 0
  
  width, height = len(matrix[0]), len(matrix)

  while width - iterations > 0 or height - iterations > 0:
    w = h = iterations

    for i in range(iterations, width):
      if matrix[h][i]:
        spiral.append(matrix[h][i])
        matrix[h][i] = False
      w = i
    for j in range(iterations + 1, height):
      if matrix[j][w]:
        spiral.append(matrix[j][w])
        matrix[j][w] = False
      h = j
    for i in range(width - 2, iterations - 1, -1):
      if matrix[h][i]:
        spiral.append(matrix[h][i])
        matrix[h][i] = False
      w = i
    for j in range(height - 2, iterations, -1):
      if matrix[j][w]:
        spiral.append(matrix[j][w])
        matrix[j][w] = False
      h = j

    if len(spiral) == len(matrix) * len(matrix[0]):
      break
  
    width, height, iterations = width - 1, height - 1, iterations + 1

  return spiral


if __name__ == "__main__":
  # print(spiral_traverse([
  #   [1, 2, 3, 4],
  #   [12, 13, 14, 5],
  #   [11, 16, 15, 6],
  #   [10, 9, 8, 7]
  # ]))

  # print(spiral_traverse([
  #   [1],
  #   [2],
  #   [3],
  #   [4],
  #   [5],
  #   [6]
  # ]))

  print(spiral_traverse([
    [1, 2, 3, 4, 5, 6, 7]
  ]))