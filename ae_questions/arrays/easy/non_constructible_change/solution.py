"""
Given an array of positive values representing the values of coins in your possession, write a function that returns the minimum amount of change that you cannot create. Coin values must be positive and don't have to be unique.
"""
def nonconstructible_change(array):
  current_min_change = sum(array) + 1

  array = sorted(array, reverse=True)

  for i in range(1, current_min_change):
    counter = i
    for j in range(len(array)):
      if counter - array[j] >= 0:
        counter -= array[j]
        if counter == 0:
          break
    
    if counter > 0:
      return i

  return current_min_change


if __name__ == "__main__":
  print(nonconstructible_change([5, 7, 1, 1, 2, 3, 22]))