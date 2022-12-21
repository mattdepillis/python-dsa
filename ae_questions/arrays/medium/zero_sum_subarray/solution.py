"""

"""
def zero_sum_subarray(array):
  if 0 in array: return True

  while len(array) > 0:
    s = sum(array)
    if s == 0: return True
    else:
      closest_index = 0 if abs(s - array[0]) <= abs(s - array[len(array) - 1]) else len(array) - 1
      array.pop(closest_index)

  return False


if __name__ == "__main__":
  print(zero_sum_subarray(
    # [-5, -5, 2, 3, -2]
    # [1]
    # [1, 2, 3]
    # [0, 0, 0]
    # [1, 2, -2, 3]
    [2, 3, 4, -5, -3, 4, 5] # should return True
  ))