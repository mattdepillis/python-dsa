"""

"""
def dfs(x, y, matrix, visited):
  print(f"x: {x}, y: {y}")
  # if the x or y coord not in the confines of the matrix, return 0
  if x not in range(len(matrix[0])) or y not in range(len(matrix)) or matrix[y][x] != 1 or (x, y) in visited : return 0

  ac = 0

  visited += [(x, y)]

  # left, right, top, bottom
  neighbors = [[-1, 0], [1, 0], [0, -1], [0, 1]]
  for neighbor in neighbors:
    ac += dfs(x + neighbor[0], y + neighbor[1], matrix, visited)

  print('ac', ac)

  return 1 + ac

def river_sizes(matrix):
  rivers, visited = [], []
  width, height = len(matrix[0]), len(matrix)
  for y in range(height):
    for x in range(width):
      if (x, y) not in visited and matrix[y][x] == 1:
        rivers += [dfs(x, y, matrix, visited)]
  print('\nr:', rivers, '\n')
  return rivers


if __name__ == "__main__":
  print(river_sizes([
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0]
  ]))