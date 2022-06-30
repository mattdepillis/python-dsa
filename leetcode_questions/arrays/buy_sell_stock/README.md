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
- O(n) time ?
  - 
- O(n) space ?
  - 