"""
Given an array prices where prices[i] is a stock's price on the ith day,
return the maximum profit you could achieve from a buy-sell transaction.
"""
def max_profit(prices):
  if len(prices) < 2:
    return 0

  max_profit, min_price = 0, prices[0]

  for price in prices:
    max_profit = max(max_profit, price - min_price)
    min_price = min(min_price, price)
  
  return max_profit
  

if __name__ == "__main__":
  print(max_profit([7,1,5,3,6,4]))
  print(max_profit([7,6,4,3,1]))