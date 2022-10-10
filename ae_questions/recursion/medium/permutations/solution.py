"""
Given an array of integers, find all the possible permutations of those integers (i.e. all the ways they can be uniquely arranged).
TC: O(n*n!), SC: O(n*n!)
"""
def get_permutations(array, arr, r):
  # return condition is: array is empty + temp array has length
  # guarantees all elements in the temp array
  if not len(array) and len(arr):
    r.append(arr)
  else:
    for item in array:
      new_array = [x for x in array if x != item]
      new_arr = arr + [item]
      # calling r.append(get_permutations(...)) here will cause circular reference,
      # appending r itself to r (resulting in [...] inclusion in the final returned value).
      # instead, simply recurse a level down and return once return condition hits.
      get_permutations(new_array, new_arr, r)

  return r


if __name__ == "__main__":
  print('\n', get_permutations(
    [1, 2, 3],
    arr=[],
    r=[]
  ))