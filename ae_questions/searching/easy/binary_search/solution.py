"""
Write a function that takes a sorted array of integers and a target integer to find, and uses a binary search algorithm to assess whether or not the number is in the array.
"""
def binary_search(array, target):
  start, end = 0, len(array) - 1

  while start <= end:
    mid = (start + end) // 2
    guess = array[mid]

    if guess > target:
      end = mid - 1
    elif guess < target:
      start = mid + 1
    else:
      return mid

  return -1


if __name__ == "__main__":
  print(binary_search([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 34))