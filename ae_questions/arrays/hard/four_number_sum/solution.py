"""
Given a non-empty array of distinct integers and target sum, return all possible 4-number sums equivalent to the target in a 2-dimensional array.

TC:
SC:
"""
def three_number_sum(array, target):
  s = []

  for i in range(len(array) - 2):
    store = {}
    for j in range(i + 1, len(array)):
      if array[j] in store:
        s.append(store[array[j]] + [array[j]])
      diff = target - (array[i] + array[j])
      store[diff] = [array[i], array[j]]
  return s


def four_number_sum(array, target):
  sums = []
  for i in range(len(array) - 3):
    three_nums = three_number_sum(array[i + 1:], target - array[i])
    for three in three_nums:
      three.append(array[i])
    sums += three_nums
  return sums


if __name__ == "__main__":
  print(four_number_sum([7, 6, 4, -1, 1, 2], 16))