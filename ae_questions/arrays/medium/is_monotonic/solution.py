"""
Write a function that takes in an array of integers and determines whether or not the array is monotonic - that is, whether each of its array elements (left to right) are non-increasing or non-decreasing.

For example, ```is_monotonic([-1, -5, -10, -1100, -1100, -1101, -1102, -9001])``` should return ```true``` because all elements are equal to or less than the previous item.

TC: O(n)
SC: O(1)
"""
def is_monotonic(array):
  if len(array) < 2:
    return True

  direction = None
  for i in range(1, len(array) - 1):
    d = "less" if array[i] < array[i - 1] else "more" if array[i] > array[i - 1] else "equal"
    if d is not "equal":
      if not direction:
        direction = d
      elif d != direction:
        return False
  return True

if __name__ == "__main__":
  print(is_monotonic([-1, -5, -10, -1100, -1100, -1101, -1102, -9001])) # true
  print(is_monotonic([1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 7, 9, 10, 11])) # false
  print(is_monotonic([1, 2])) # true