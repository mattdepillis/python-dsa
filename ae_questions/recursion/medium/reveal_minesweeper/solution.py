"""
Given a clicked spot on the board, will reveal the number of adjacent mines to the spot according to the rules of the [Minesweeper](https://en.wikipedia.org/wiki/Minesweeper_(video_game)) game.

Rules:
- "M" = mine
- "H" = unrevealed spot on board

If the clicked spot on the board isn't a mine, determine how many adjacent mines there are. If adjacent mines are 0, recurse to neighbors until we reveal spots with at least one mine adjacent.

TC: O(w * h), where w = width and h = height of matrix
SC: O(w * h)
"""
def find_neighbors(board, row, col):
  """ Finds valid neighbors for the current spot on the board. """
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
  """ Determines how many mines lie adjacent to the current spot on the board. Recurses to neighbors if 0. """
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
  """ Handler function. """
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