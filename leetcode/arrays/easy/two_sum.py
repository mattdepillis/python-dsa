"""
  * my initial array-based successful leetcode solution
  * stats: 14MB memory (97.90%), 5197ms runtime (12.90%)
"""
class InitialSolution(object):

  def twoSum(self, nums, target):
    for i in range(len(nums)):
      # cut the array to iterate over by all previous and current indices
      arr_to_iterate = nums[i+1:]

      for num in range(len(arr_to_iterate)):
        if nums[i] + arr_to_iterate[num] == target:
          j = i + num + 1
          return [i, j]

"""
  * alternative hash table (dict) solution
"""
class AltSolution(object):
  def twoSum(self, nums, target):
    item_info = {}
    for i, value in enumerate(nums):
      # can calculate the required matching number for this particular value
      diff = target - value

      # if in the dict, return indices
      if diff in item_info:
        return [item_info[diff], i]
      else:
        item_info[value] = i


# test solution
if __name__ == "__main__":
  # print(InitialSolution().twoSum([1, 2, 3, 4, 6], 9))
  print(AltSolution().twoSum([1, 2, 3, 4, 6], 9))