"""
Write a function that performs binary search on an array of distinct integers, but with the caveat that the numbers are shifted x spots such that the min and max may not be at the beg/end of the array. Return the index of the target number if found, and -1 if not.

TC: O(log(n)) -- roughly log(n) iterations through the list to find a val
SC: O(1) -- done in-place
"""
def is_between_middle_and_end(array, target, middle, end):
  """
  if middle is less than end:
  - target must be in between or equal to end

  if middle is greater than end:
  - target must be greater than middle or less than end
  """
  greater_middle = array[middle] > array[end]

  return (
    target > array[middle] or target <= array[end]
  ) if greater_middle else (
    array[middle] < target <= array[end]
  )

def shifted_binary_search(array, target):
  start, end = 0, len(array) - 1

  while start <= end:
    middle = (start + end) // 2
    if array[middle] == target: return middle
    elif is_between_middle_and_end(array, target, middle, end):
      start = middle + 1
    else: end = middle - 1

  return -1


if __name__ == "__main__":
  print(shifted_binary_search(
    [45, 61, 71, 72, 73, 0, 1, 21, 33, 37],
    21
  ))