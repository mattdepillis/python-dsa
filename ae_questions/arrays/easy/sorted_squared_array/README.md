---
Problem: Sorted Squared Array
Type: Array
Date Written: 07-11-2022
---

# Problem
Write a function that takes a non-empty, unsorted array of integers and returns an array of same length containing those numbers squared and sorted.

For example, python```sorted_squared_array([2, 3, 1, 5, 6, 4])``` should return ```[1, 4, 9, 16, 25, 36]```.

# Solution
My initial solution to this problem is a simple one-liner that makes use of Python's built-in python```sorted()``` method.

**Pseudocode:**
- create a new array of squares for each number in the array.
- sort the array with the python```sorted()``` method.

**Big O:**
- O(n*log(n)) time
  - sorting algorithms have worst-case time complexity of O(n*log(n)).
- O(n) space
  - it creates and returns a new array of size n