---
Problem: Best Time to Buy and Sell Stock (Max Profit)
Type: Array
Date Written: 06-30-2022
---

# Problem
Given an array prices where prices[i] is a stock's price on the ith day, return the maximum profit you could achieve from a buy-sell transaction.

For example, python```max_profit([7,1,5,3,6,4])``` should return ```5```.

# Solution
I chose to use a similar approach to the max_sum problem - create a variable ```max_profit``` that tracks the current max profit found by buying a share of stock and selling on a later date. I figured I wouldn't need a different data structure to efficiently solve the problem - I could traverse the array, calculating the relative max at each index and comparing to the current value of ```max_profit```.

**Pseudocode:**
- create a variable ```max_profit``` to track the current max profit observed for a given buy date (index) i, and set it to 0.
- traverse through the array by index.
- find the max future price of the array after this current date (index) by calling python```max(prices[i + 1:])``` - this creates a sliced array from the next index onward (future values) and finds the max value in this subarray.
- if the profit python```max_future_price - priceAtCurrentDate``` is greater than the current value of max_profit, then overwrite max profit with this value. Else, continue.

**Big O:**
- O(n^2) time
  - with this approach, at each index we perform a copy on the array into a new variable, which is roughly an O(n) time operation. Since we loop through each index, an O(n) operation for each index results in O(n^2) runtime.
- O(n^2) space
  - because this solution requires copying a slice of the array into memory for each index, the memory requirements will surge to roughly n^2 proportions.

**Issues With this Approach:**
- Copying a slice of the array into memory at each index is an incredibly expensive operation that will increase runtime dramatically as the size of the list increases. This problem could instead be solved in a single-pass manner with inexpensive operations at each index.

# Revised Solution, and Why it Improves on the First
A better solution would be to use a tracking variable for minimum price in addition to the already-declared ```max_profit``` variable. At each list price, we can perform two operations to determine max profit in one pass with inexpensive operations:
  1. recalculate ```max_profit``` as the max of the current value of max profit, and the difference between this price and the current value of ```min_price```.
  2. recalculate ```min_price``` as the min of the current min price and the current price.
The comparison operations are much more inexpensive than the prior list slicing + copying solution.

**Pseudocode:**
- define tracking variables ```min_price``` and ```max_profit```.
- loop through list values.
- at each value:
  - recalculate ```max_profit``` as the max of the current value of max profit, and the difference between this price and the current value of ```min_price```.
  - recalculate ```min_price``` as the min of the current min price and the current price.

**Big O:**
- O(n) time
  - operations inside the loop are O(1) time-complex, since they're simple min-max operations. This cuts the time complexity of the algorithm down to O(n).
- O(1) space
  - The algorithm will always store values for the two tracking variables and nothing else. No matter the list's size, memory used will stay constant.