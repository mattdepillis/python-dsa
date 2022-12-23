"""
Given a non-empty array of distinct integers and target sum, return all possible 4-number sums equivalent to the target in a 2-dimensional array.

TC:
SC:
"""
def four_number_sum(array, target):
  sums, store = [], {}

  for i in range(len(array)):
    temp_store = {}
    print(f"array[i]: {array[i]}, store: {store}")
    for s in store:
      ts_key = target - (sum(store[s]) + array[i])
      temp_store[ts_key] = store[s] + [array[i]]
      
      if len(temp_store[ts_key]) == 4:
        if sum(temp_store[ts_key]) == target: sums.append(temp_store[ts_key])
        del temp_store[ts_key]

    store.update(temp_store)
    store[array[i]] = [array[i]]

  return sums


if __name__ == "__main__":
  # print(four_number_sum([7, 6, 4, -1, 1, 2], 16))
  print(four_number_sum([5, -5, -2, 2, 3, -3], 0))