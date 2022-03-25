"""
Given an int[] nums, find the contiguous subarray of at least one number with the largest sum and return its sum.
"""

"""
Original solution: implemented correctly but runtime not O(n) -- poor performance on large arrays.
"""
class Solution(object):
  def maximumSubArray(self, nums):
    max_sum = None

    for size in range(1, len(nums) + 1):
      for i in range(len(nums)):
        if len(nums[i:size]) > 0:
          if (max_sum == None or sum(nums[i:size]) > max_sum):
            max_sum = sum(nums[i:size])

    return max_sum

"""
Found solution in O(n) time -- loop over each array item.
  * determine whether or not the current number is greater than the current number + sum of previous nums
  * determine whether the current num/sum is greater than the current maximum value
"""
# think about runtime in O(n) terms -- previous solution far too slow for large arrays
class RevisedSolution(object):
  def maxSubArray(self, nums):
    if not nums:
      return 0

    current_sum = max_sum = nums[0]
    for num in nums[1:]:
      # check if the current number is greater than all the numbers before it combined
      # set it as current sum if true, to reset the index of the subarray
      # if false, add it to the subarray
      print('cs', current_sum)
      print('num', num)
      current_sum = max(num, current_sum + num)
     
      # then, check if the current_sum just determined is greater than the current max
      # if not, the subarray is cut at the previous 
      max_sum = max(current_sum, max_sum)

    return max_sum


if __name__ == "__main__":
  # print(Solution().maximumSubArray([-2,-1]))
  print(RevisedSolution().maxSubArray([2, 3, -4, 3, -2, 6, -2]))
