"""
Write a function that takes an array of positive integers and returns the maximum sum of non-adjacent array elements.

Solution: create an array of max length 2. Add each new number to the first sum if array of sums length < 2.
If the combined sum is less than the previous sum, add the previous sum back to the array in the place of the combined sum as the current prevailing max sum.

TC: O(n), SC: O(1)
"""
def max_subset_sum_no_adjacent(array):
  sums = [0]

  for num in array:
    if len(sums) < 2:
      sums.append(num)
    else:
      new_sum = sums[0] + num
      if new_sum < sums[1]:
        new_sum = sums[1]
      sums[0], sums[1] = sums[1], new_sum

  return max(sums)


if __name__ == "__main__":
  print(max_subset_sum_no_adjacent([75, 105, 120, 75, 90, 135]))