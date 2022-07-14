"""
Write a function that takes an array of integers and returns that array sorted using an insertion sort algorithm.
"""
def insertion_sort(array):
  if len(array) < 2:
    return array
  
  slice_at = len(array) // 2
  sorted_array, unsorted_array = sorted(array[ : slice_at]), array[slice_at : ]

  for i in unsorted_array:
    for j in range(len(sorted_array)):
      if sorted_array[j] > i:
        sorted_array.insert(j, i)
        break
      elif j == len(sorted_array) - 1:
        sorted_array.append(i)

  return sorted_array

if __name__ == "__main__":
  # print(insertion_sort([1, 8, 2, 6, 4, 5, 10, 7, 9]))
  print(insertion_sort([1]))