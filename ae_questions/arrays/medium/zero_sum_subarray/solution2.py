"""
Given a list of integers, write a function that returns a boolean indicating whether or not there's a subarray of the array that sums to 0. Valid subarrays can range from length 1 to the length of the array itself.

* I thought of this idea initially, but using an array (not set) as the intermediary DS.
* Set lookups run in O(1) time (array lookups in O(n) time) -- consider this for future. 

TC: O(n)
SC: O(n)
"""
def zero_sum_subarray(array):
  """
  If the sum at the current number equals a number that's already in the set,
  you know the nums between the number that put the value into the set and this
  one sum to zero!
  """
  sums = set({0})
  current = 0
  for num in array:
    current += num
    # lookup of item in set is O(1)
    if current in sums: return True
    sums.add(current)

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