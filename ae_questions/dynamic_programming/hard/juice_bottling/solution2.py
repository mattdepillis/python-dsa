"""
Complete solution.

TC: O(n^2) -- need to loop through all numbers max n times
SC: O(n) -- max calls on the stack is n at a given time
"""
def recurse(prices, units_left):
  max_revenue = 0
  max_indices = []

  for i in reversed(range(1, units_left + 1)):
    revenue, indices = prices[i], [i]
    remaining = units_left - i
    if remaining > 0:
      add_revenue, add_indices = recurse(prices, remaining)
      revenue += add_revenue
      indices += add_indices

    if revenue > max_revenue:
      max_revenue, max_indices = revenue, indices

  return max_revenue, max_indices



def juice_bottling(prices):
  return sorted(recurse(prices, len(prices) - 1)[1])

if __name__ == "__main__":
  print(juice_bottling(
    [0, 1, 3, 7, 5, 4, 12, 15, 20, 18, 25]
  ))