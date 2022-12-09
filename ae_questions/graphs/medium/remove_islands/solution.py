"""

"""
def dfs(i, j, valid_indices, matrix, visited):
  pairs_to_check = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]

  for (x, y) in pairs_to_check:
    if (x, y) not in visited and matrix[x][y] == 1:
      if (x, y) in valid_indices or dfs(x, y, valid_indices, matrix, visited + [(x, y)]):
        valid_indices.add((i, j))
        return True
  return False


def remove_islands(matrix):
  valid_indices = set()

  for i in range(len(matrix)):
    r = range(len(matrix[i])) if i == 0 or i == len(matrix) - 1 else (0, len(matrix[i]) - 1)
    for j in r:
      if matrix[i][j] == 1:
        valid_indices.add((i, j))

  for i in range(1, len(matrix) - 1):
    for j in range(1, len(matrix[i]) - 1):
      if matrix[i][j] == 1:
        if not (i, j) in valid_indices and not dfs(i, j, valid_indices, matrix, visited=[(i, j)]):
          matrix[i][j] = 0

  return matrix


if __name__ == "__main__":
  print(remove_islands([
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1]
  ]))