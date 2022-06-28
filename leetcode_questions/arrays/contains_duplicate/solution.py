"""
original solution to contains_duplicate.
creates dict of unique elements for quicker lookup than for-loop given large array.
"""
def contains_duplicate(nums):
  uniques = {}
  for i in range(len(nums)):
    if nums[i] in uniques:
      return True
    uniques[nums[i]] = nums[i]
  return False
    

if __name__ == "__main__":
  # print(contains_duplicate([1,2,3,1]))
  # print(contains_duplicate([1,2,3,4]))
  # print(contains_duplicate([1,1,1,3,3,4,3,2,4,2]))
  print(contains_duplicate([7, 0, 1, 4, 5]))
  # print(contains_duplicate([0]))