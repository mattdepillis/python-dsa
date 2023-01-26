"""
Write a function that takes a matrix of integers -- the matrix rows can be of unequal length -- and return the min number of passes required to convert all negative integers in the matrix positive.
"""
def determine_adjacent(i, j, matrix):
  return [
    [i, j - 1] if j > 0 else None, # left
    [i, j + 1] if j < len(matrix[i]) - 1 else None, # right
    [i - 1, j] if i > 0 else None, # up
    [i + 1, j] if i < len(matrix) - 1 else None
  ]

def min_passes_of_matrix(matrix):
  passes = 0
  while True:
    change, to_change = [], 0
    for i in range(len(matrix)):
      for j in range(len(matrix[i])):
        if matrix[i][j] >= 0: continue
        adjacents = determine_adjacent(i, j, matrix)
        for pair in adjacents:
          if pair is None: continue
          if matrix[pair[0]][pair[1]] > 0:
            change += [[i, j]]
            to_change += 1
            break
    if to_change < 1: break
    for pair in change: matrix[pair[0]][pair[1]] *= -1
    passes += 1
    
  return -1 if not passes else passes
      

if __name__ == "__main__":
  print(min_passes_of_matrix([
    [0, -1, -3, 2, 0],
    [1, -2, -5, -1, -3],
    [3, 0, 0, -4, -1]
  ])) # 3

  # v = min_passes_of_matrix([
  #   [0, -1, -3, 2, 0],
  #   [1, -2, -5, -1, -3],
  #   [3, 0, 0, -4, -1]
  # ])

  # for row in v: print(row)