"""
Given a non-empty array of positive integers, where each int represents the max # of steps forward in the array from that index that can be taken, return the minimum number of jumps needed to get from the starting to ending indices of the array.

TC: O(n)
SC: O(m), where m = minimum jumps (must hold m recursive calls on the stack)
"""
def recurse(array, i):
  max_jumps = array[i]
    
  if i + max_jumps >= len(array) - 1: return 1

  max_in_range, jump_to_idx = 0, i

  for j in range(i + 1, i + max_jumps + 1):
    if array[j] >= max_in_range or j - jump_to_idx >= max_in_range:
        max_in_range, jump_to_idx = array[j], j

  if jump_to_idx >= len(array) - 1: return 1

  return recurse(array, jump_to_idx) + 1

def min_number_of_jumps(array):
  return 0 if len(array) < 2 else recurse(array, 0)


if __name__ == "__main__":
  print(min_number_of_jumps([3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3])) # 4
  print(min_number_of_jumps([2, 1, 2, 3, 1])) # 2
  print(min_number_of_jumps([2, 1, 2, 3, 1, 1, 1])) # 3
  # print(min_number_of_jumps([3, 12, 2, 1, 2, 3, 15, 1, 1, 1, 3, 2, 3, 2, 1, 1, 1, 1]))
  print(min_number_of_jumps([3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3, 2, 3, 2, 1, 1, 1, 1])) # 7
  print(min_number_of_jumps([3, 10, 2, 1, 2, 3, 7, 1, 1, 1, 3, 2, 3, 2, 1, 1, 1, 1])) # 6
  print(min_number_of_jumps([3, 12, 2, 1, 2, 3, 7, 1, 1, 1, 3, 2, 3, 2, 1, 1, 1, 1])) # 5