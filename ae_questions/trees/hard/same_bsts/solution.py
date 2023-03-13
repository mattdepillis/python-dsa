"""

"""
def find_next_node(array, index, last_common, direction):
  return (
    direction == 'left' and array[index] <= last_common
  ) or (
    direction == 'right' and array[index] > last_common
  )

def recurse(one, one_index, one_visited, two, two_index, two_visited, value, direction):
  min_index = min(one_index, two_index)

  # print(f"one: {one}, one_visited: {one_visited}, two: {two}, two_visited: {two_visited}, two_index: {two_index}, value: {value}, direction: {direction}")

  one_next = two_next = None
  one_next_index = two_next_index = None

  for i in range(min_index + 1, len(one)):
    if not one_next and i > one_index and not one_visited[i]:
      if find_next_node(one, i, value, direction):
        one_next, one_next_index = one[i], i
    if not two_next and i > two_index and not two_visited[i]:
      if find_next_node(two, i, value, direction):
        two_next, two_next_index = two[i], i

    # print('ot', one_next, two_next, one_next_index, two_next_index)

    if one_next and two_next: break

  # print("one and two next:", one_next, two_next)

  if one_next == two_next:
    if not one_next: return True
    
    one_visited[one_next_index], two_visited[two_next_index] = True, True
    
    return recurse(
      one, one_index, one_visited, two, two_index, two_visited, one_next, 'left'
    ) and recurse(
      one, one_index, one_visited, two, two_index, two_visited, one_next, 'right'
    )
  return False
  
def generate_visited(array):
  return [True] + [False for _ in range(len(array) - 1)]

def same_bsts(one, two):
  if not len(one) == len(two) or not one[0] == two[0]:
    return False
  
  one_visited, two_visited = generate_visited(one), generate_visited(two)

  one_index, two_index, common = 0, 0, one[0]
  
  return recurse(
    one, one_index, one_visited, two, two_index, two_visited, common, 'left'
  ) and recurse(
    one, one_index, one_visited, two, two_index, two_visited, common, 'right'
  )

if __name__ == "__main__":
  # print(same_bsts(
  #   [10, 15, 8, 12, 94, 81, 5, 2, 10],
  #   [10, 8, 5, 15, 2, 10, 12, 94, 81]
  # )) # False
  # print(same_bsts(
  #   [10, 15, 8, 12, 94, 81, 5, 2, 11],
  #   [10, 8, 5, 15, 2, 12, 11, 94, 81]
  # )) # True

  # TODO get this to return True
  print(same_bsts(
    [10, 15, 8, 12, 94, 81, 5, 2, -1, 100, 45, 12, 8, -1, 8, 2, -34],
    [10, 8, 5, 15, 2, 12, 94, 81, -1, -1, -34, 8, 2, 8, 12, 45, 100]
  ))
