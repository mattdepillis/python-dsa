"""
Write a function that takes in an array of distinct integers and a target sum, and returns all the possible combinations of three numbers that sum to the target sum as an array of arrays. Make sure that child arrays are sorted smallest to largest, and that the parent array is as well.
"""
def three_number_sum(array, target):
  results = []

  for i in range(len(array) - 2):
    combinations = {}
    for j in range(i + 1, len(array)):
      if array[j] in combinations:
        combinations[array[j]].append(array[j])
        results.append(sorted(combinations[array[j]]))
      diff = target - (array[i] + array[j])
      combinations[diff] = [array[i], array[j]]
  
  return sorted(results)


if __name__ == "__main__":
  print(three_number_sum([12, 3, 1, 2, -6, 5, -8, 6], 0)) # sorted -> [-8, -6, 1, 2, 3, 5, 6, 12]
  print(three_number_sum([1, 2, 3], 6))