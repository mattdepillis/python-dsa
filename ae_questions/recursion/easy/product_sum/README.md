---
Problem: Product Sum
Type: Recursion
Date Written: 08-28-2022
---

# Problem
Write a function that takes in an array of integers and nested arrays containing integers and other nested arrays, and returns the product sum where nested arrays are summed and then multiplied by their level of depth.

For example, python```product_sum([5, 2, [7, -1], 3, [6, [-13, 8], 4]])``` should return ```12```.

# Solution
I used...

**Pseudocode:**
- 

**Big O:**
- O(n) time
  - 
- O(d) space, where d is the max depth of the array + its subarrays
  - 

**Issues With this Approach:**
- 

# Revised Solution, and Why it Improves on the First
Instead, we can use...

**Pseudocode:**
- 

**Big O:**
- O(n) time
  - 
- O(1) space
  - 