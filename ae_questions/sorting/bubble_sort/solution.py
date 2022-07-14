"""
Write a function that takes an array of integers and returns that array sorted using a bubble sort algorithm.
"""
def bubble_sort(array):
  iterations = 0
  swapped = True

  while(swapped):
    swapped = False
    for i in range(len(array) - iterations - 1):
      if array[i] > array[i + 1]:
        swapped = True
        array[i], array[i + 1] = array[i + 1], array[i]
  
  return array

 
if __name__ == "__main__":
  print(bubble_sort([1, 8, 2, 6, 4, 5, 10, 7]))