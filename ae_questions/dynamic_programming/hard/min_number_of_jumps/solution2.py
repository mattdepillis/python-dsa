"""
Given a non-empty array of positive integers, where each int represents the max # of steps forward in the array from that index that can be taken, return the minimum number of jumps needed to get from the starting to ending indices of the array.

TC: O(n)
SC: O(1)
"""
def min_number_of_jumps(array):
  jumps = 0
  max_reach = steps_to_take = array[0]

  for i in range(1, len(array) - 1):
    max_reach = max(max_reach, i + array[i])
    steps_to_take -= 1
    if steps_to_take == 0:
      jumps += 1
      # set steps_to_take to the max_reach beyond this sequence of steps - the index you're currently at
      steps_to_take += max_reach - i

  return jumps + 1


if __name__ == "__main__":
  print(min_number_of_jumps([3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3])) # 4
  print(min_number_of_jumps([2, 1, 2, 3, 1])) # 2
  print(min_number_of_jumps([2, 1, 2, 3, 1, 1, 1])) # 3
  # print(min_number_of_jumps([3, 12, 2, 1, 2, 3, 15, 1, 1, 1, 3, 2, 3, 2, 1, 1, 1, 1]))
  print(min_number_of_jumps([3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3, 2, 3, 2, 1, 1, 1, 1])) # 7
  print(min_number_of_jumps([3, 10, 2, 1, 2, 3, 7, 1, 1, 1, 3, 2, 3, 2, 1, 1, 1, 1])) # 6
  print(min_number_of_jumps([3, 12, 2, 1, 2, 3, 7, 1, 1, 1, 3, 2, 3, 2, 1, 1, 1, 1])) # 5