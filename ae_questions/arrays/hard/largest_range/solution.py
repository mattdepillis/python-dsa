"""
Write a function that takes an array of integers and returns an array of len=2 representing the largest range of consecutive integers in the array.

TC: O(n) -- loop through all array elements multiple times
SC: O(n) -- need to create neg and pos, which sum to n elements
"""

# helper function to determine whether to include a number in the most recent range, or to create a new one
# handles both negative and positive integer values
def evaluate_num(num, ranges, longest):
  if not len(ranges):
    ranges += [[num, num]]
  else:
    if num < 0 and num == ranges[0][0] - 1:
      ranges[0][0] = num
    elif num >= 0 and num == ranges[-1][1] + 1:
      ranges[-1][1] = num
    else:
      r = [[num, num]]
      ranges = r + ranges if num < 0 else ranges + r

  comp = ranges[0] if num < 0 else ranges[-1]
  range_diff = abs(comp[1] - comp[0])
  if not len(longest[1]) or range_diff > longest[0]:
    longest = [range_diff, comp]

  return ranges, longest


def largest_range(array):
  neg, pos = set({abs(x) for x in array if x < 0}), set({x for x in array if x >= 0})
  ranges, longest = [], [0, []]

  for num in neg: ranges, longest = evaluate_num(-num, ranges, longest)
  for num in pos: ranges, longest = evaluate_num(num, ranges, longest)
  
  return longest[1]


if __name__ == "__main__":
  # print(largest_range([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]))
  # print(largest_range([1, 1, 1, 3, 4]))
  # print(largest_range([0, 9, 19, -1, 18, 17, 2, 10, 3, 12, 5, 16, 4, 11, 8, 7, 6, 15, 12, 12, 2, 1, 6, 13, 14, -23]))
  # print(largest_range([-7, -7, -7, -7, 8, -8, 0, 9, 19, -1, -3, 18, 17, 2, 10, 3, 12, 5, 16, 4, 11, -6, 8, 7, 6, 15, 12, 12, -5, 2, 1, 6, 13, 14, -4, -2]))
  # print(largest_range([8, 4, 2, 10, 3, 6, 7, 9, 1]))
  print(largest_range([0, -5, 9, 19, -1, 18, 17, 2, -4, -3, 10, 3, 12, 5, 16, 4, 11, 7, -6, -7, 6, 15, 12, 12, 2, 1, 6, 13, 14, -2]))