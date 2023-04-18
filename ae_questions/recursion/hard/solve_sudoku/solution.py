"""

"""
def find_possible_values(matrix):
  integers = set({ 1, 2, 3, 4, 5, 6, 7, 8, 9 })
  found = set()
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      if matrix[i][j] != 0: found.add(matrix[i][j])
  return integers - found


def find_possibilities(board, row_index, col_index):
  row_start = 0 if row_index <= 2 else 3 if row_index <= 5 else 6
  col_start = 0 if col_index <= 2 else 3 if col_index <= 5 else 6

  row = board[row_index]
  col = [row[col_index] for row in board]

  square = [board[i][j]
    for i in range(row_start, row_start + 3)
    for j in range(col_start, col_start + 3)
  ]

  return find_possible_values([row, col, square])


def solve(board, row, col):
  if row == 9: return board, True

  if board[row][col] != 0: return solve(
    board,
    row if col < 8 else row + 1,
    col + 1 if col < 8 else 0
  )
  possible_values = find_possibilities(board, row, col)

  if len(possible_values) == 0: return board, False
  for i in possible_values:
    # TODO: how to make a shallow copy of board?
    b = board
    b[row][col] = i
    filled_board, success = solve(
      b,
      row if col < 8 else row + 1,
      col + 1 if col < 8 else 0
    )
    print(f"row,col: {row},{col}, value tried: {i}")
    if success:
      return filled_board, True
  return board, False


def solve_sudoku(board):
  return solve(board, 0, 0)


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