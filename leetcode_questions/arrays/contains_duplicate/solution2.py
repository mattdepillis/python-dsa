"""
revised solution for contains_duplicate (much faster, same memory allocation).
uses the built-in set data structure, which stores unique values in unordered fashion.
"""
def contains_duplicate(nums):
  unique_length = len(set(nums))
  return len(nums) >= 2 and unique_length < len(nums)

if __name__ == "__main__":
  print(contains_duplicate([0]))
  print(contains_duplicate([3, 3]))