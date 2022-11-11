"""
Given an array of integers, sort it using the selection sort algorithm.

TC: O(n^2) -- we need to iterate through each index n times -- leading to a n^2 TC
SC: O(n) -- storing values in new array. We can actually do better than this - I thought I was shooting for optimal SC = O(n).
"""
def selection_sort(array):
  sorted = []
  while len(array):
    min_value, min_index = array[0], 0

    for i in range(1, len(array)):
      if array[i] < min_value:
        min_value, min_index = array[i], i

    sorted.append(min_value)
    array.pop(min_index)

  return sorted


if __name__ == "__main__":
  print(selection_sort(
    [8, 5, 2, 9, 5, 6, 3]
  ))