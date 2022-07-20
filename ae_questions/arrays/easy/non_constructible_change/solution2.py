"""
Given an array of positive values representing the values of coins in your possession, write a function that returns the minimum amount of change that you cannot create. Coin values must be positive and don't have to be unique.
"""
def nonconstructible_change(array):
  array.sort()
  minimum_change = 0
  for i in array:
    if i > minimum_change + 1:
      break
    minimum_change += i
  return minimum_change + 1


if __name__ == "__main__":
  print(nonconstructible_change([5, 7, 1, 1, 2, 3, 22]))