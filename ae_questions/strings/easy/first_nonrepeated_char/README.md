---
Problem: First Nonrepeating Character in String
Type: String
Date Written: 08-12-2022
---

# Problem
Write a function that takes in a string of lowercase English letters and returns the index of the string's first non-repeating character. If there is no non-repeating character, return -1.

For example, python```non_repeating_character('hello')``` should return ```0```.

# Solution
I chose to use a dict to store each unique character and its frequency counter. Now that Python dicts are ordered, I could guarantee that, once all items had been placed in the characters dict, the first character I found in it with a frequency of 1 was the corrrect first nonrepeating character in the string.

**Pseudocode:**
- initialize a dict ```chars``` to hold the frequency of each character in the string.
- loop over each char in the string:
  - if the character isn't a dict key, add it and init its value to 0.
  - regardless, increment the value 1.
- loop through the dict. For the first value you find == 1, return the string index of the char.
- else, return -1. 

**Big O:**
- O(n + m) time, where n = length of string and m = unique chars in the dict
  - we must iterate over each item in the string and then each k-v pair in the dict in the worst case.
- O(c) space, where c is the number of unique chars in the string (worst-case: O(n))
  - we must init a dict that contains a key-value pair for each unique char in the string.