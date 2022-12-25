"""
Given a non-empty array of distinct integers and target sum, return all possible 4-number sums equivalent to the target in a 2-dimensional array.

NOTE: this solution improves upon solution1 from a TC standpoint.

TC:
  - O(n^2) average: if there aren't any matches (or few to average), the line
    ```for combo in store[s]```
    will run infrequently.
  - O(n^3) worst: if there are nearly (or completely) all matches on that for-loop, the function will run in O(n^3) time.
SC:
  - O(n^2) -- need to store a combo of each pair of numbers in the dict
"""
def four_number_sum(array, target):
  store, sums = {}, []

  """
  At a given number in the array,
    - loop through its successor values
    - at each one, see if the sum of the two vals is in the store
    - append each pair at that sum in the store to sums with sum included
  For all numbers that came before it,
    - create an array pair and add it to the store key based on target - sum(pair)
  """
  for i in range(len(array) - 1):
    for j in range(i, len(array)):
      s = array[i] + array[j]
      if s in store:
        for combo in store[s]:
          sums.append(combo + [array[i], array[j]])

    for k in range(0, i):
      diff = target - (array[k] + array[i])
      if not diff in store:
        store[diff] = [[array[k], array[i]]]
      else: store[diff] += [[array[k], array[i]]]

  return sums


if __name__ == "__main__":
  print(four_number_sum([7, 6, 4, -1, 1, 2], 16))
  # print('\n', four_number_sum([5, -5, -2, 2, 3, -3], 0))