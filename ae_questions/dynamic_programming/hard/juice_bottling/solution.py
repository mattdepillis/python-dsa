"""

"""
def juice_bottling(prices):
  optimal = []
  units = len(prices) - 1

  while units > 0:
    idx, optimal_number = 0, 0
    purchase_power_at_units = [0 for _ in range(units + 1)]
    possible = prices[:units + 1]
    for i in range(1, len(possible)):
      power = possible[i] / i
      if power > optimal_number: idx, optimal_number = i, power
      purchase_power_at_units[i] = power

    optimal += [idx]
    units -= idx

  return sorted(optimal)


if __name__ == "__main__":
  print(juice_bottling(
    [0, 1, 3, 2]
  )) # [1, 2]

  print(juice_bottling(
    [0, 2, 3, 4]
  )) # [1, 1, 1]

  print(juice_bottling(
    [0, 5, 6, 7, 8, 9, 10]
  )) # [1, 1, 1, 1, 1, 1]

  print(juice_bottling(
    [0, 1, 3, 5, 4, 10, 7, 12, 15, 13, 16]
  )) # [5, 5]

  print(juice_bottling(
    [0, 1, 3, 6, 5, 4, 17, 15, 20, 18, 21]
  )) # [1, 3, 6]