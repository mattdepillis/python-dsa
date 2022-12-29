"""

"""
def subarray_sort(array):
  unsorted_end = -1
  unsorted_min = unsorted_max = None

  for i in range(1, len(array)):
    if unsorted_end >= 0:
      if array[i] > unsorted_max: unsorted_max = array[i]
      elif array[i] < unsorted_max:
        unsorted_end = i
        if array[i] < unsorted_min: unsorted_min = array[i]
    elif array[i] < array[i - 1]:
      unsorted_end, unsorted_min, unsorted_max = i, array[i], array[i - 1]

  for i in range(len(array)):
    if unsorted_min and array[i] > unsorted_min:
      return[i, unsorted_end]

  return [-1, -1]


if __name__ == "__main__":
  # print(subarray_sort(
  #   [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
  # ))
  print(subarray_sort([2, 1]))