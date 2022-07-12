"""
Implementation of a bubble sort algorithm in Python.
Big O:
- time complexity: O(n^2)
- space complexity: O(1)
"""
def bubble_sort(array):
  swapped = True
  iterations = 0

  while(swapped):
    swapped = False
    for j in range(len(array) - iterations - 1):
      if array[j] > array[j + 1]:
        array[j], array[j + 1] = array[j + 1], array[j]
        swapped = True
    iterations += 1

  return array


if __name__ == "__main__":
  print(bubble_sort([1, 8, 2, 6, 4, 5, 10, 7]))
  print(bubble_sort([19, 13, 6, 2, 18, 8]))