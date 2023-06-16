"""

"""
def find_neighbors(board, row, col):
  neighbors = []
  last_row, last_col = len(board) - 1, len(board[0]) - 1

  potential_neighbors = [(row, col - 1), (row, col + 1), # left, right
                         (row - 1, col - 1), (row - 1, col), (row - 1, col + 1), # row above: L C R
                         (row + 1, col - 1), (row + 1, col), (row + 1, col + 1) # row below: L C R
  ]
  for pair in potential_neighbors:
    if (not 0 <= pair[0] <= last_row) or (not 0 <= pair[1] <= last_col): continue
    neighbors.append(pair)

  return neighbors


def find_adjacent_mines(board, row, col, visited):
  if (row, col) in visited: return
  visited.append((row, col))

  neighbors = find_neighbors(board, row, col)

  adjacent_mines = 0
  for n in neighbors:
    if board[n[0]][n[1]] == "M": adjacent_mines += 1

  if adjacent_mines == 0:
    for n in neighbors: find_adjacent_mines(board, n[0], n[1], visited)

  board[row][col] = f"{adjacent_mines}"


def reveal_minesweeper(board, row, col):
  # check clicked spot for mine
  if board[row][col] == "M":
    board[row][col] = "X"
    return board
  
  find_adjacent_mines(board, row, col, visited=[])

  return board


if __name__ == "__main__":
  print(reveal_minesweeper([
    ["H", "H", "H", "H", "M"],
    ["H", "H", "M", "H", "H"],
    ["H", "H", "H", "H", "H"],
    ["H", "H", "H", "H", "H"]
  ], 3, 0))