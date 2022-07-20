"""
Write a function that takes a non-empty, unsorted array of integers and returns an array of same length containing those numbers squared and sorted.
"""
def sorted_squared_array(array):
  return sorted([i ** 2 for i in array])


if __name__ == "__main__":
  print(sorted_squared_array([2, 3, 1, 5, 6, 4]))