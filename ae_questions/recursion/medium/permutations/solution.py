"""
Given an array of integers and a target integer, return the array such that all instances of that integer are found at the end of the array.
TC: O(n*n!), SC: O(n*n!)
"""
def get_permutations(array, arr, r):
  if not len(array) and len(arr):
    r.append(arr)
  else:
    for item in array:
      new_array = [x for x in array if x != item]
      new_arr = arr + [item]
      get_permutations(new_array, new_arr, r)

  return r


if __name__ == "__main__":
  print('\n', get_permutations(
    [1, 2, 3],
    arr=[],
    r=[]
  ))