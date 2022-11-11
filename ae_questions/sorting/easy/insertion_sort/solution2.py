"""
Write a function that takes an array of integers and returns that array sorted using an insertion sort algorithm.
"""
def insertion_sort(array):
  for i in range(1, len(array)):
    current = array[i]

    while i > 0 and array[i - 1] > current:
      print(i)
      array[i] = array[i - 1]
      i -= 1
    
    array[i] = current
    
  return array

if __name__ == "__main__":
  # print(insertion_sort([1, 8, 2, 6, 4, 5, 10, 7, 9]))
  print(insertion_sort([1]))