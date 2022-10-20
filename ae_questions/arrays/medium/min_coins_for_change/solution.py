"""
Given an array of positive integers, each representing a denomination of a coin value (there is an infinite amount of each coin), return the minimum number of coins needed to make change for a target amount. If change cannot be made, return -1.

NOTE: this only solves 16/17 cases -- needed modified solution to complete.
"""

def min_coins_for_change(n, coins):
  sorted_coins, ledger, min_coins = sorted(coins, reverse=True), [], -1

  for coin in sorted_coins:
    target, used = n, 0
    while coin <= target:
      target, used = target - coin, used + 1

    for entry in ledger:
      t, u = entry[0], entry[1]
      while coin <= t:
        t, u = t - coin, u + 1
      if t == 0:
        if min_coins < 0 or u < min_coins:
          min_coins = u
    
    for entry in ledger:
      if entry[0] == 0:
        ledger.remove(entry)

    if target == 0:
      if min_coins < 0 or used < min_coins:
          min_coins = used
    else:
      ledger.append([target, used])

  return min_coins


if __name__ == "__main__":
  # print(min_coins_for_change(7, [1, 5, 10])) # 3
  # print(min_coins_for_change(0, [1, 2, 3])) # may have to return -1 for this case
  # print(min_coins_for_change(7, [2, 4])) # -1
  # print(min_coins_for_change(10, [1, 3, 4])) # 4
  # print(min_coins_for_change(9, [3, 5])) # 3
  # print(min_coins_for_change(10, [1, 5, 7])) # 2
  print(min_coins_for_change(10, [1, 3, 4])) # ! not solvable with this code