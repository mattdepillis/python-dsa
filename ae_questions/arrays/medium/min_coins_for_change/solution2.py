"""
Given an array of positive integers, each representing a denomination of a coin value (there is an infinite amount of each coin), return the minimum number of coins needed to make change for a target amount. If change cannot be made, return -1.

TC: O(n * c), where n = target and c = number of coins.
SC: O(n)
"""
def min_coins_for_change(n, coins):
  num_coins = [0] + [float('inf') for _ in range(n)]
  for coin in coins:
    for amount in range(len(num_coins)):
      if coin <= amount:
        num_coins[amount] = min(num_coins[amount], num_coins[amount - coin] + 1)
  return num_coins[n] if num_coins[n] != float('inf') else -1

if __name__ == "__main__":
  print(min_coins_for_change(10, [1, 3, 4]))