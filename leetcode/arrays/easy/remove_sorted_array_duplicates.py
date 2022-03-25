"""
For an ascending sorted array, remove any duplicate elements in place.
Return the number of unique elements in the array.
Memory should not be allocated for an additional array; the provided array should be modified.
  * e.g. if [1, 2, 2, 3, 4] provided, final array should look like the following: [1, 2, 3, 4]
"""

"""
  * initial solution using a hash table (dict)
  * stats: 17.5MB memory (10.08%), 119ms runtime (38.08%)
"""
class Solution(object):
  def removeDuplicates(self, nums):
    track = {}
    c = 0
    for i, val in enumerate(nums):
      if val in track:
        nums[i] = '_'
        c += 1
      else:
        track[val] = i

    # False < True, so ints will be sorted to the front of the array
    nums.sort(key=lambda x: isinstance(x, str))
    nums = nums[:len(nums) - c]
    return len(nums)

# test example
if __name__ == "__main__":
  print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))