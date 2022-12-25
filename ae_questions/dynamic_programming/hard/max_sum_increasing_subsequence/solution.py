"""
Write a function that takes a list of integers and returns the greatest sum that can be generated from a subsequence of the array consisting of strictly increasing values.
"""
def max_sum_increasing_subsequence(array):
  subarrays, max_subsequence = [[array[0]]], [0, []]
  
  for i in range(1, len(array)):
    added = False
    for subarray in subarrays:
      if array[i] > subarray[-1]:
        subarray.append(array[i])
        added = True
    if not added:
      new_subarray = [array[i]]
      for j in reversed(range(0, i)):
        if array[j] < new_subarray[0]: new_subarray.insert(0, array[j])
      subarrays.append(new_subarray)

  for subarray in subarrays:
    if sum(subarray) > max_subsequence[0]: max_subsequence = [sum(subarray), subarray]

  return max_subsequence

if __name__ == "__main__":
  print(max_sum_increasing_subsequence([10, 70, 20, 30, 50, 11, 30])) # [110, [10, 20, 30, 50]]