"""

"""
def quick_sort(array):
  if len(array) < 2: return array

  pointer = 0
  left, right = pointer + 1, len(array) - 1

  while left <= right:
    if array[left] >= array[pointer] and array[right] < array[pointer]:
      array[left], array[right] = array[right], array[left]
      right -= 1
    else: left += 1

  print('a', array, right)

  if array[right] < array[pointer]:
    array[pointer], array[right] = array[right], array[pointer]

  if right > (len(array) - 1) - right:
    array[right + 1:] = quick_sort(array[right + 1:])
    array[:right] = quick_sort(array[:right])
  else:
    array[:right] = quick_sort(array[:right])
    array[right + 1:] = quick_sort(array[right + 1:])

  return array


if __name__ == "__main__":
  # print(quick_sort([7, 8, 5, 2, 9, 5, 6, 3]))

  print(quick_sort([1, 3, 2]))