"""
Given an array of integers and a target integer, return the array such that all instances of that integer are found at the end of the array.
TC: O(n), SC: O(1)
"""
def move_element_to_end(array, target):
  start_index = None

  for i in range(len(array)):
    if array[i] == target and start_index is None:
        start_index = i
    elif array[i] != target and start_index is not None:
        array[start_index], array[i] = array[i], array[start_index]
        # increment by 1. start_index will just resume at the same target value if there's only been one encountered,
        # or will simply pick up at the next target value as the ones before it have already been shifted ahead.
        start_index += 1

  return array

if __name__ == "__main__":
  print(move_element_to_end(
    [2, 1, 2, 2, 2, 3, 4, 2],
    2
  ))