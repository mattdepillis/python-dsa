"""
Write a function that takes 2 non-empty arrays of integers and returns an array of 2 numbers (one from each array) whose absolute difference is the smallest. The number in the first array should appear first in the return array.
"""
def smallest_difference(array1, array2):
  array1.sort(), array2.sort()
  print(array1, array2)

  smallest_diff, pair = None, []
  p1 = p2 = 0

  while p1 < len(array1) and p2 < len(array2):
    print(p1)
    diff = abs(array1[p1] - array2[p2])
    print('diff', array1[p1], array2[p2])
    if not smallest_diff or diff < smallest_diff:
      smallest_diff, pair = diff, [array1[p1], array2[p2]]

    if (p1 + 1 == len(array1) or 
        abs(array1[p1 + 1] - array2[p2]) > abs(array1[p1] - array2[p2 + 1])
    ):
      p2 += 1
    elif p2 + 1 == len(array2) or abs(array1[p1 + 1] - array2[p2]) < abs(array1[p1] - array2[p2 + 1]):
      p1 += 1
    else:
      p1, p2 = p1 + 1, p2 + 1

    # print(p1, array1[p1], array2[p2], smallest_diff, pair)

  return pair


if __name__ == "__main__":
  # print(smallest_difference(
  #   [-1, 5, 10, 20, 28, 3],
  #   [26, 134, 135, 15, 17]
  # ))

  print(smallest_difference(
    [-1, 5, 10, 20, 3],
    [26, 134, 135, 15, 17]
  ))