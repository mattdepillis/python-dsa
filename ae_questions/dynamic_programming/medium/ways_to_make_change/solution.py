"""
Given an array of coin denominations and a target amount of change to achieve, return the number of combinations from the array of coins that achieve that change number. The array of denoms represents value -- there's no limit to the number of coins at your disposal for any given denomination.

TC: O(nd), where n = change and d = size of array
SC: O(n) -- storing n + 1 elements in ways
"""
def ways_to_make_change(change, array):
  ways = [0 for _ in range(change + 1)]

  # can make 0 change one way - set this as base value
  ways[0] = 1
  for num in array:
    for amount in range(1, change + 1):
      if num <= amount:
        ways[amount] += ways[amount - num] # if num = 1, increment ways[1] by ways[0] = 1
  return ways[change]


if __name__ == "__main__":
  # print(ways_to_make_change(10, [1, 5, 10, 25]))
  # print(ways_to_make_change(0, [2, 3, 4, 7]))
  # print(ways_to_make_change(25, [1, 5, 10, 25]))
  # print(ways_to_make_change(7, [2, 3, 4, 7]))
  print(ways_to_make_change(12, [2, 3, 7]))