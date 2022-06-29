"""
returns the subarray of the provided array nums that contains the largest sum.
"""
def maximum_subarray(nums):
  start = end = 0
  current_sum = max_sum = 0

  for i in range(len(nums)):
    current_sum += nums[i]
    if nums[i] > current_sum and nums[i] > max_sum:
      start = i
      max_sum = current_sum = nums[i]
    elif max_sum <= current_sum:
      max_sum = current_sum
      end = i + 1

  return nums[start : end]
    

if __name__ == "__main__":
  print(maximum_subarray([1, -2, 2, 3, 4, -2, 1]))
  print(maximum_subarray([1, -2, 2, 3, 4, -2, 3]))
  print(maximum_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
  print(maximum_subarray([7, 0, 1, 4, 5]))
  print(maximum_subarray([7]))