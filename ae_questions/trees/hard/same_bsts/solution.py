"""

"""
def find_next_node(array, index, last_common, direction):
  return (
    direction == 'left' and array[index] <= last_common
  ) or (
    direction == 'right' and array[index] > last_common
  )

def recurse(one, one_index, two, two_index, tree_value, values, direction):
  min_index = min(one_index, two_index)
  print(f"one: {one}, one_index: {one_index}, two: {two}, two_index: {two_index}, tree_values: {tree_value}, values: {values}, direction: {direction}")
  one_next = two_next = None
  one_next_index = two_next_index = None
  for i in range(min_index + 1, len(one)):
    if not one_next and i > one_index:
      if find_next_node(one, i, tree_value, direction):
        one_next, one_next_index = one[i], i
    if not two_next and i > two_index:
      if find_next_node(two, i, tree_value, direction):
        two_next, two_next_index = two[i], i
    print('ot', one_next, two_next, one_next_index, two_next_index)
    if one_next and two_next: break

  # TODO: need to return values for 

  print("one and two next:", one_next, two_next)
  if one_next == two_next:
    if not one_next: return True, None
    is_same, val = recurse(
      one, one_next_index, two, two_next_index, one_next, values + [one_next],'left'
    )
    if is_same and not val: return True
    return is_same and recurse(
      one, one_next_index, two, two_next_index, one_next, values + [one_next],'right'
    )


def same_bsts(one, two):
  if not len(one) == len(two) or not one[0] == two[0]:
    return False

  one_stack, two_stack, common, vals = [0], [0], one[0], [one[0]]
  
  # return recurse(
  #   one, one_stack[0], two, two_stack[0], common, 'left'
  # ) and recurse(
  #   one, one_stack[0], two, two_stack[0], common, 'right'
  # )

  left_same, val = recurse(
    one, one_stack[0], two, two_stack[0], common, vals, 'left'
  )
  print('LEFT', left_same)
  if left_same and not val:
    right_same, val = recurse(
      one, one_stack[0], two, two_stack[0], common, vals, 'right'
    )
    return right_same
  return False

if __name__ == "__main__":
  print(same_bsts(
    [10, 15, 8, 12, 94, 81, 5, 2, 10],
    [10, 8, 5, 15, 2, 10, 12, 94, 81]
  ))