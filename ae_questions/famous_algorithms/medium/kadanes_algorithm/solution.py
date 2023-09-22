"""
Solve the max-subarray problem with Kadane's algorithm.

Solution 1: my own. One pass. TC = O(n), SC = O(1)
"""
def kadanes_algorithm(array):
  min_sum = total_sum = 0
  max_subarray_sum = array[0]

  for i in range(len(array)):
    total_sum += array[i]
    if total_sum - min_sum > max_subarray_sum:
      max_subarray_sum = total_sum - min_sum
    if total_sum < min_sum: min_sum = total_sum
  
  return max_subarray_sum


if __name__ == "__main__":
  print(kadanes_algorithm(
    [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
  ))

  print(kadanes_algorithm(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  ))

  print(kadanes_algorithm(
    [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
  ))