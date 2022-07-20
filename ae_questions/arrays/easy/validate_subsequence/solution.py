"""
Given two non-empty arrays of integers, determine whether the second is a valid subsequence of the first. A valid subsequence means the numbers in the sequence must all appear in the exact same order in the array.
"""
def validate_subsequence(array, sequence):
  if len(array) == 0 or len(sequence) == 0:
    raise Exception("Array and sequence must both have length of at least 1.")
  
  for num in sequence:
    try:
      index = array.index(num)
      array = array[index + 1:]
    except ValueError:
      return False
  
  return True
    

if __name__ == "__main__":
  print(validate_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))
  print(validate_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, -1]))