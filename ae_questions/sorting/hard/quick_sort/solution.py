"""
Write a QuickSort algorithm to sort an input array of integers, from smallest to largest.

TC:
  - Best/Average: O(n * log(n)) -- iterate through log(n) elements on average (split of array into L and R), n times
  - Worst: O(n^2) -- array is already perfectly sorted or totally reversed
SC:
  - O(log(n)) -- we hold at maximum log(n) to n (but average = log(n)) calls on the stack at a given time due to partitioning of array and recursion
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

  if array[right] < array[pointer]:
    array[pointer], array[right] = array[right], array[pointer]
    pointer = right

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