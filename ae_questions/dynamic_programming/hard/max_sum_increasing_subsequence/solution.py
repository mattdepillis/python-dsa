"""
Write a function that takes a list of integers and returns the greatest sum that can be generated from a subsequence of the array consisting of strictly increasing values.

TC: O(n^2) -- at any given index i, may have to perform multiple O(n) operations (merging arrays, resetting array contents, etc.)
SC: O(n) -- storage proportional to the number of items in the input array
"""
def max_sum_increasing_subsequence(array):
  """
  Logic:
  - Create max_subseq + backup subseq and track their sums
  - keep track of last index at which a merge occurs (start at 0)
  - if array[i] is greater than last num of max sub, add it
  - if not, gets added to the end of the backup array
  - merge if backup sum is greater than max sum, and reset max and backup arrays
  """

  max_sum, backup_sum = array[0], 0
  max_subsequence, backup_subsequence = [array[0]], []
  merge_index = 0

  for i in range(1, len(array)):
    if array[i] > max_subsequence[-1]:
      if max_sum < 0:
        max_subsequence, max_sum = [array[i]], array[i]
        continue
      max_subsequence += [array[i]]
      max_sum += array[i]
    else:
      backup_subsequence = [x for x in backup_subsequence if x < array[i]] + [array[i]]
      backup_sum = sum(backup_subsequence)

      if backup_sum > max_sum:
        merged = max_subsequence[:merge_index - 1] + [y for y in backup_subsequence if y > max_subsequence[merge_index]]
        merged_sum = sum(merged)

        max_subsequence, max_sum = (merged, merged_sum) if merged_sum > backup_sum else (backup_subsequence, backup_sum)

        backup_subsequence, backup_sum = [x for x in max_subsequence], max_sum
        merge_index = len(max_subsequence) - 1

  return [max_sum, max_subsequence]

if __name__ == "__main__":
  print(max_sum_increasing_subsequence([10, 70, 20, 30, 50, 11, 30])) # [110, [10, 20, 30, 50]]
  print(max_sum_increasing_subsequence([-1, 1]))
  print(max_sum_increasing_subsequence([-5, -4, -3, -2, -1]))
  print(max_sum_increasing_subsequence([8, 12, 2, 3, 15, 5, 7]))
  print(max_sum_increasing_subsequence([10, 15, 4, 5, 11, 14, 31, 25, 31, 23, 25, 31, 50]))