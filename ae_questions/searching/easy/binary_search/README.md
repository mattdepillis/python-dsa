---
Problem: Binary Search
Type: Search
Date Written: 07-20-2022
---

# Problem
Write a function that takes a sorted array of integers and a target integer to find, and uses a binary search algorithm to assess whether or not the number is in the array.

For example, python```binary_search([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33)``` should return ```3```.

# Solution
A binary search algorithm, on every iteration, should guess that the middle index of the array is the target number. If the index = the target, the index is returned. Else, the array should shrink to narrow the searchable range for the next iteration.

I use the classic two-pointer approach to this problem. The idea: create pointer values to track the current start and end indices to search in the array. While the start index is less than or equal to the end index, I calculate the middle integer index of the array by averaging start and end. Then, I set my guess equal to the value of the middle index. If the guess is equal to the target value, I return the middle index (index of my guess). Else, if the guess is higher than the target, I shrink the searchable array by setting the end index to the middle index - 1. Same logic if the guess is lower: I move the start index to middle index + 1.

If the target is never found, I return -1 to signify the target's absence from the array.

**Pseudocode:**
- set start index equal to 0 and end index equal to python```len(array) - 1```.
- while the start index is less than or equal to the end index:
  - calculate the middle index to observe by averaging start and end.
  - set guess equal to python```array[mid]```.
  - if guess > target, move start index up to ```mid + 1```.
  - else if guess < target, move end index back to ```mid - 1```.
  - else, the guess and target are equal. Return python```mid```, the guess' index.
- if start > end and the target has not been found, the target isn't in the array. return -1

**Big O:**
- O(log(n)) time
  - in the worst case, this algorithm takes log(n) cutting operations to arrive at the proper value. For example, for array python```[1, 2, 3, 4, 5, 6, 7, 8]``` of length 8, the maximum number of cuts the algorithm will make to the observable array is 3, which is the base-2 log of 8.
- O(1) space
  - the only memory allocated is toward the init variables + mid - therefore, the space complexity is constant no matter the size of the array.