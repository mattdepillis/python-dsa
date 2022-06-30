"""
Given an array prices where prices[i] is a stock's price on the ith day,
return the maximum profit you could achieve from a buy-sell transaction.
"""
def max_profit(prices):
  max_profit = 0

  for i in range(len(prices) - 1):
    max_future_price = max(prices[i + 1:])
    if max_future_price - prices[i] > max_profit:
      max_profit = max_future_price - prices[i]
  
  return max_profit
  

if __name__ == "__main__":
  print(max_profit([7,1,5,3,6,4]))
  print(max_profit([7,6,4,3,1]))
