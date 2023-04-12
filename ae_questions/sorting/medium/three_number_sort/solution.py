"""

"""
def three_number_sort(array, order):
  placed = 0
  for i in range(len(order) - 1):
    for j in range(len(array)):
      if order[i] == array[j]:
        if j == placed: continue
        array[placed], array[j] = array[j], array[placed]
        placed += 1
  return array


if __name__ == "__main__":
  print(three_number_sort(
    [1, 0, 0, -1, -1, 0, 1, 1],
    [0, 1, -1]
  )) # [0, 0, 0, 1, 1, 1, -1, -1]

  # print(three_number_sort(
  #   [0, 1],
  #   [1, 2, 0]
  # ))

  print(three_number_sort(
    [9, 9, 9, 7, 9, 7, 9, 9, 7, 9],
    [7, 11, 9]
  ))