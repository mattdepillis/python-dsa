"""
Given two arrays of integers:
- first: all integers are guaranteed to be in the second
- second: unique integers; represents the desired sorted order of ints in the first,
sort the first array according to the order of the second. Do so in place (don't create a new array).

TC: O(n) -- need to iterate through the array just twice
SC: O(1)
"""
def three_number_sort(array, order):
  placed = 0
  for i in range(len(order) - 1):
    for j in range(len(array)):
      if order[i] == array[j]:
        array[placed], array[j] = array[j], array[placed]
        placed += 1
  return array


if __name__ == "__main__":
  # print(three_number_sort(
  #   [1, 0, 0, -1, -1, 0, 1, 1],
  #   [0, 1, -1]
  # )) # [0, 0, 0, 1, 1, 1, -1, -1]

  # print(three_number_sort(
  #   [0, 1],
  #   [1, 2, 0]
  # ))

  # print(three_number_sort(
  #   [9, 9, 9, 7, 9, 7, 9, 9, 7, 9],
  #   [7, 11, 9]
  # ))

  print(three_number_sort(
    [-2, -3, -3, -3, -3, -3, -2, -2, -3],
    [-2, -3, 0]
  ))