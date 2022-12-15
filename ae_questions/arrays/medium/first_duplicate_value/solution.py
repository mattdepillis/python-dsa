"""
Given an array of integers with values between 1 and n, where n is the length of the array, write a function that returns the first integer that appears more than once.

Optimal TC: O(n)
Optimal SC: O(1)
"""

# O(n) ST solution
def first_duplicate_value(array):
  s = set()
  for i in array:
    if i in s:
      return i
    s.add(i)

  return -1


# O(n^2) TC, O(1) SC
# def first_duplicate_value(array):
#   for i in range(len(array)):
#     if isinstance(array[i], list): continue
#     for j in range(i + 1, len(array)):
#       if array[j] == array[i]:
#         array[j] = [array[j]]
#         break

#   for i in array:
#     if isinstance(i, list): return i[0]
#   return -1


if __name__ == "__main__":
  print(first_duplicate_value([2, 1, 5, 2, 3, 3, 2, 4]))