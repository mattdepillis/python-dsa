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
    elif array[right] >= array[pointer]: right -= 1
    else: left += 1

  print('a', array, right)

  if array[right] < array[pointer]:
    array[pointer], array[right] = array[right], array[pointer]
    pointer = right

  print('p', pointer, array[pointer], array)

  if pointer > (len(array) - 1) - pointer:
    array[pointer + 1:] = quick_sort(array[pointer + 1:])
    array[:pointer] = quick_sort(array[:pointer])
  else:
    array[:pointer] = quick_sort(array[:pointer])
    array[pointer + 1:] = quick_sort(array[pointer + 1:])

  return array


if __name__ == "__main__":
  # print(quick_sort([7, 8, 5, 2, 9, 5, 6, 3]))

  # print(quick_sort([1, 3, 2]))

  print(quick_sort([5, -2, 2, -8, 3, -10, -6, -1, 2, -2, 9, 1, 1]))