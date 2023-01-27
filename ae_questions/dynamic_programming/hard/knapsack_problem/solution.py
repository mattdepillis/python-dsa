"""
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
