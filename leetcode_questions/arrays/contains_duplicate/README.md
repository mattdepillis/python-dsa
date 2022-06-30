---
Problem: Contains Duplicate
Type: Array
Date Written: 06-29-2022
---

# Problem
Given an array of integers, return a boolean True or False to indicate whether or not the provided array contains any duplicates. The array should be at least two elements long in order to return True.

For example, python```contains_duplicate([7, 0, 1, 4, 5])``` should return ```False```.

# Solution
I chose to use a dict to store all previously-encountered array values in the first solution to this problem. The use of a hash table seemed like a good choice because hash table search takes O(1) time.

**Pseudocode:**
- define a hash table ```uniques```.
- loop though each array index.
- if the integer at array index i ```nums[i]``` is found in uniques, return True.
- else, add ```nums[i]``` to the dict: ```uniques[nums[i]] = nums[i]```.
- if no duplicates are found, return False.

**Big O:**
- O(2n) -> O(n) time
  - need to loop over each array element
  - lookup in dict is constant time for each array element
- O(n) space
  - need to store values in dict

**Issues With this Approach:**
- It's inefficient. With a pure dict, I had to give each key a value, which costs time + memory and was inconsequential in solving the problem. A dict was not the ideal data structure to help me solve this problem.

# Revised Solution, and Why it Improves on the First
Instead, we can use a set, which is a built-in Python data type that's essentially an abstraction of a hash table: it stores unique keys without values. This is a more ideal data structure for this problem because:
  1. it can be initialized in one O(n) operation, and
  2. no additional operations are required to add meaningless values to unique keys
A set yields the same time complexity O(n) as the hash table, but in reality runs much faster, as it takes just O(n) time to initialize compared to the O(2n) time it takes to loop through an array and then check for a duplicate in a hash table + add the number if it doesn't yet exist.

**Pseudocode:**
- convert the array to a set, and store the length of the set in the variable ```unique_length```.
- if the array length is greater than 2 and ```unique_length < len(array)```, return True - there are duplicates.
- Else, return False.

**Big O:**
- O(n) time
  - need to convert the array into a modified hash table (Set), which takes O(n) time for ~n operations
- O(n) space
  - set conversion takes up O(n) space