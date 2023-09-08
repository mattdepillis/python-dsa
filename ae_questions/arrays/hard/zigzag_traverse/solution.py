"""

"""
def determine_next_move(moves, matrix, prev_move, current_indices):
  return


def zigzag_traverse(matrix):
  visited, curr = [], [0, 0]
  moves = [
    [0, 1], # down
    [1, -1], # up and right
    [1, 0], # right
    [-1, 1] # down and left
  ]
  next_move = moves[0]

  # for i in range(len(matrix) * len(matrix[0])):
  for i in range(0, 1):
    visited.append(matrix[curr[0]][curr[1]])
    curr = [
      curr[0] + next_move[0],
      curr[1] + next_move[1]
    ]
    print('new_curr', curr)

    next_move = determine_next_move(moves, matrix, next_move, curr)
    
  return visited


if __name__ == "__main__":
  print(zigzag_traverse([
    [1, 3, 4, 10],
    [2, 5, 9, 11],
    [6, 8, 12, 15],
    [7, 13, 14, 16]
  ]))