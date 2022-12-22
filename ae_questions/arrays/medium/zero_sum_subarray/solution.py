"""

"""
def zero_sum_subarray(array):
  if 0 in array: return True

  while len(array) > 0:
    s = sum(array)
    if s == 0: return True
    else:
      start, end = 0, len(array) - 1
      closest_index = start if abs(s - array[start]) <= abs(s - array[end]) else end

      num_to_check = len(array) // 2
      check = array[:num_to_check] if closest_index == end else array[-num_to_check]
      if isinstance(check, list):
        check_sum = 0
        for i in range(len(check)):
          check_sum += check[i]
          if check_sum == s:
            closest_index = start if closest_index == end else end
            break
 
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