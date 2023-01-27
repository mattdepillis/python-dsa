"""
Given:
  - an array of subarrays with 2 items per subarray: value and weight of an item, and
  - a total weight capacity of items that a knapsack can hold,

return the optimal value of items that can be held in the knapsack, along with an array of indices representing each included item's index in the original items array.

TC: O(n*c) -- where n = number of items and c = total capacity
SC: O(n*c) -- where n = number of items and c = total capacity
"""
def recurse(scale, candidates, capacity_remaining, optimal):
  o = optimal
  for i, candidate in enumerate(candidates):
    value, weight = candidate
    if weight <= capacity_remaining:
      c = [c for c in candidates[i:] if c != candidate]
      x = recurse(
        scale + i + 1, c, capacity_remaining - weight, [o[0] + value, o[1] + [i + scale]]
      )
      if x[0] > optimal[0]: optimal = x
  return optimal

def knapsack_problem(items, capacity):
  return recurse(0, items, capacity, [0, []])


if __name__ == "__main__":
  print(knapsack_problem(
    [[1, 2], [4, 3], [5, 6], [6, 7]],
    10
  ))
