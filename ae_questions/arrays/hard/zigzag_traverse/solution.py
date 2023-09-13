"""

"""
def is_move_valid(matrix, indices):
  print(indices[0], indices[1])
  # if indices[0] >= len(matrix) or indices[0] >= len(matrix[indices[0]]) or indices[0] < 0: return False
  if indices[0] >= len(matrix) or indices[0] < 0: return False
  if indices[1] >= len(matrix[indices[0]]) or indices[1] < 0: return False
  if matrix[indices[0]][indices[1]] is None: return False
  return True

def determine_next_move(moves, matrix, prev_move, current_indices):
  try_next = prev_move + 1 if (prev_move % 2 == 0 or prev_move < 0) else prev_move

  for _ in range(4):
    circular_index = try_next % 4
    # print('ci', circular_index, current_indices)
    indices = [
      current_indices[0] + moves[circular_index][0],
      current_indices[1] + moves[circular_index][1]
    ]
    # print('i', indices)
    if is_move_valid(matrix, indices): return circular_index
    try_next += 1
  
  return try_next % 4


def zigzag_traverse(matrix):
  visited, curr = [], [0, 0]
  moves = [
    [1, 0], # down
    [-1, 1], # up and right
    [0, 1], # right
    [1, -1] # down and left
  ]
  next_move = -1

  for _ in range(len(matrix) * len(matrix[0])):
    print('trying to add', curr[0], curr[1])
    visited.append(matrix[curr[0]][curr[1]])
    print("new move! ", visited)

    next_move = determine_next_move(moves, matrix, next_move, curr)
    print('actual next move', next_move)

    new_indices = [
      curr[0] + moves[next_move][0],
      curr[1] + moves[next_move][1]
    ]
    matrix[curr[0]][curr[1]] = None
    curr = new_indices
    print('new curr', curr)

    # next_move = determine_next_move(moves, matrix, next_move, curr)
    # print('nm', next_move)
    
  return visited


if __name__ == "__main__":
  print(zigzag_traverse([
    [1, 3, 4, 10],
    [2, 5, 9, 11],
    [6, 8, 12, 15],
    [7, 13, 14, 16]
  ]))

  print(zigzag_traverse([
    [1],
    [2],
    [3],
    [4]
  ]))

  print(zigzag_traverse([
    [1, 2, 3, 4, 5]
  ]))