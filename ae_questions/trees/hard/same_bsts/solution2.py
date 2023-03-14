"""
If an array of integers represents a valid BST, write a function that takes 2 separate arrays and returns a boolean value representing the equality of the two trees.

TC: O(n)
SC: O(n)
"""
# must be smaller than previous number and greater than or equal to min at this level
def get_smaller_index(array, index, value):
  for i in range(index + 1, len(array)):
    if array[i] < array[index] and array[i] >= value:
      return i
  return -1

# must be greater than or equal to prior number and smaller than max at this level
def get_larger_index(array, index, value):
  for i in range(index + 1, len(array)):
    if array[i] >= array[index] and array[i] < value:
      return i
  return -1

# min, max value set a value range for each recursive call to find left or right node
def recurse(one, two, index_one, index_two, min_value, max_value):
  if index_one == -1 or index_two == -1: return index_one == index_two
  if one[index_one] != two[index_two]: return False

  left_index_one, left_index_two = get_smaller_index(one, index_one, min_value), get_smaller_index(two, index_two, min_value)
  right_index_one, right_index_two = get_larger_index(one, index_one, max_value), get_larger_index(two, index_two, max_value)

  return recurse(
    one, two, left_index_one, left_index_two, min_value, one[index_one]
  ) and recurse(
    one, two, right_index_one, right_index_two, one[index_one], max_value
  )


def same_bsts(one, two):
  return recurse(one, two, 0, 0, float('-inf'), float('inf'))


if __name__ == "__main__":
  print(same_bsts(
    [10, 15, 8, 12, 94, 81, 5, 2, -1, 100, 45, 12, 8, -1, 8, 2, -34],
    [10, 8, 5, 15, 2, 12, 94, 81, -1, -1, -34, 8, 2, 8, 12, 45, 100]
  ))