"""
Given a non-empty array of distinct integers and target sum, return all possible 4-number sums equivalent to the target in a 2-dimensional array.

NOTE: solution1 is much better from a complexity standpoint.

TC:
  - O(n * (2^n)) -- need to repeat loop for each item; at each loop, there are more and more combinations needed to be traversed
SC:
  - O(2^n) -- need to create a new array in the store from each item in already in the store by the new item.
"""
def four_number_sum(array, target):
  store = {}

  for i in range(len(array)):
    temp_store = {}
    for s in store:
      for si in range(len(store[s])):
        ts_key = (sum(store[s][si]) + array[i])

        if not ts_key in temp_store: temp_store[ts_key] = [store[s][si] + [array[i]]]
        else: temp_store[ts_key] += [store[s][si] + [array[i]]]

    for item in temp_store:
      if not item in store: store[item] = temp_store[item]
      else: store[item] += temp_store[item]

    if not array[i] in store: store[array[i]] = [[array[i]]]
    else: store[array[i]] += [[array[i]]]

  return [s for s in store[target] if len(s) == 4] if target in store else []


if __name__ == "__main__":
  print(four_number_sum([7, 6, 4, -1, 1, 2], 16))
  print('\n', four_number_sum([5, -5, -2, 2, 3, -3], 0))