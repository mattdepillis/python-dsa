"""
Given an array of integers, sort it using the selection sort algorithm.

TC: O(n^2) -- we need to iterate through each index n times -- leading to a n^2 TC
SC: O(1) -- storing values in new array. We can actually do better than this - I thought I was shooting for optimal SC = O(n).
"""
def selection_sort(array):
  for i in range(len(array)):
    min_value, min_index = array[i], i
    for j in range(i, len(array)):
      if array[j] < min_value:
        min_value, min_index = array[j], j

    array[i], array[min_index] = array[min_index], array[i]

  return array


if __name__ == "__main__":
  print(selection_sort(
    [8, 5, 2, 9, 5, 6, 3]
  ))