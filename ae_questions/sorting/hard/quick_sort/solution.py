"""

"""
def quick_sort(array):
  pointer = 0
  left = pointer + 1 if not len(array) <= 2 else pointer
  right = len(array) - 1

  while left <= right:
    if array[left] >= array[pointer] and array[right] < array[pointer]:
      array[left], array[right] = array[right], array[left]
      right -= 1
    else:
      left += 1

  array[pointer], array[right] = array[right], array[pointer]

  return array


if __name__ == "__main__":
  print(quick_sort([7, 8, 5, 2, 9, 5, 6, 3]))