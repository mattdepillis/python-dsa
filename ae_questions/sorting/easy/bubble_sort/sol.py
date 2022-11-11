"""
Bubble sort recap.
"""
def bubble_sort(array):
  iterations, sorted = 0, True
  while sorted:
    sorted = False
    for i in range(len(array) - iterations - 1):
      if array[i] > array[i + 1]:
        sorted = True
        array[i], array[i + 1] = array[i + 1], array[i]
    iterations += 1

  return array


if __name__ == "__main__":
  print(bubble_sort(
    [8, 5, 2, 9, 5, 6, 3]
  ))