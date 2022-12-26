"""
Write a function that takes a list of integers and returns the greatest sum that can be generated from a subsequence of the array consisting of strictly increasing values.

TC: O(n^2) -- at any given index i, may have to perform multiple O(n) operations
SC: O(n) -- storage proportional to the number of items in the input array
"""
def max_sum_increasing_subsequence(array):
  """
  Logic:
  - 
  """

  return

if __name__ == "__main__":
  print(max_sum_increasing_subsequence([10, 70, 20, 30, 50, 11, 30])) # [110, [10, 20, 30, 50]]
  print(max_sum_increasing_subsequence([-1, 1]))
  print(max_sum_increasing_subsequence([-5, -4, -3, -2, -1]))
  print(max_sum_increasing_subsequence([8, 12, 2, 3, 15, 5, 7]))
  print(max_sum_increasing_subsequence([10, 15, 4, 5, 11, 14, 31, 25, 31, 23, 25, 31, 50]))