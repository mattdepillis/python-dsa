"""
Given two non-empty arrays of integers, determine whether the second is a valid subsequence of the first. A valid subsequence means the numbers in the sequence must all appear in the exact same order in the array.
"""
def validate_subsequence(array, sequence):
  j = 0

  for i in range(len(array)):
    if j == len(sequence):
      break
    elif array[i] == sequence[j]:
      j += 1

  return j == len(sequence)

if __name__ == "__main__":
  print(validate_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))
  print(validate_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, -1]))