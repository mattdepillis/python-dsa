"""
Write a function that takes a list of integers and returns the length of the longest peak in the array, defined as adjacent integers in the array that are strictly increasing until they reach a tip, at which point they become strictly decreasing.

TC: O(n)
SC: O(1)
"""
def longest_peak(list):
  increasing, valid = True, False
  longest = current = 0

  for i in range(0, len(list) - 1):
    current += 1
    if increasing:
      if list[i] == list[i + 1]: current = 0
      elif list[i] > list[i + 1]:
        if current > 1: increasing, valid = False, True
        else: current = 0
    else:
      if list[i] <= list[i + 1]:
        if current > longest: longest = current
        current = 0 if list[i] == list[i + 1] else 1
        increasing, valid = True, False

  return longest if longest >= current + 1 or not valid else current + 1


if __name__ == "__main__":
  # print(longest_peak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3])) # 6
  print(longest_peak([1, 3, 2])) # 3
  # print(longest_peak([5, 4, 3, 2, 1, 2, 10, 12])) # 0
  # print(longest_peak([1, 1, 3, 2, 1])) # 4
  # print(longest_peak([1, 2, 3, 4, 5, 6, 10, 100, 1000])) # 0