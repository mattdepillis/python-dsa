"""
Given a matrix that represents a sudoku board, write a function to resolve the board.
Slots in the board = 0 must be resolved to a digit 1-9.
You may assume that each board does have a unique solution.

TC: O(1) -- set number of possibilities (9x9 grid)
SC: O(1) -- set number of possibilities (9x9 grid)
"""

def is_valid(board, row_index, col_index, digit):
  """
  Checks the row, column, and square for the target digit.
  Returns True if it's valid (digit isn't already found).
  """

  if digit in board[row_index]: return False
  if digit in map(lambda r: r[col_index], board): return False

  row_start = 0 if row_index <= 2 else 3 if row_index <= 5 else 6
  col_start = 0 if col_index <= 2 else 3 if col_index <= 5 else 6

  square = [board[i][j]
    for i in range(row_start, row_start + 3)
    for j in range(col_start, col_start + 3)
  ]
  if digit in square: return False

  return True


def solve(board, row, col):
  """
  Recursively solves the board.
  If a number exists in the [row][col] spot, recurse to next place.
  Else, loop through all ints 1-9 and check whether a given digit is valid.
  If no solution found at [row][col], will backtrack to try different digit combinations. 
  """

  if row == 9: return board, True

  if board[row][col] != 0: return solve(
    board,
    row if col < 8 else row + 1,
    col + 1 if col < 8 else 0
  )
 
  for i in range(1, 10):
    if is_valid(board, row, col, i):
      board[row][col] = i
      if solve(
        board,
        row if col < 8 else row + 1,
        col + 1 if col < 8 else 0
      ): return True
    
  board[row][col] = 0
  return False

# main function - run initial solve and return the board
def solve_sudoku(board):
  solve(board, 0, 0)
  return board


if __name__ == "__main__":
  print(solve_sudoku([
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
  ]))