# a more elegant, one-pass solution for two_number_sum.
# creates a dict of matches that would satisfy the target sum.
# if the current elem matches a key in diffs, return corresponding [key, value] pair.
# else, add [target_sum - elem, elem] as k/v pair to the dict
# if no matches by the end, return an empty array.
def two_number_sum(array, target_sum):
  diffs = {}
  for elem in array:
    if elem in diffs:
      return [elem, diffs[elem]]
    diffs[target_sum - elem] = elem
  return []
    

if __name__ == "__main__":
  print(two_number_sum([3, 5, -4, 8, 11, 1, -1, 6], 10))
  print(two_number_sum([4, 6], 10))
  print(two_number_sum([4, 6, 1], 5))
  print(two_number_sum([14], 15))
  print(two_number_sum([3, 5, -4, 8, 11, 1, -1, 6], 15))