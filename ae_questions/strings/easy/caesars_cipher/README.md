---
Problem: Caesar's Cipher
Type: String
Date Written: 08-07-2022
---

# Problem
Write a function that takes a string and an integer key and returns the string shifted in Caesar's Cipher method by y spots equaling the value of the key.

For example, python```caesars_cipher('abc', 3)``` should return ```'def```.

# Solution

**Pseudocode:**
- Initialize a new string.
- For each letter in the loop:
  - Figure out what index of the alphabet that letter is (0-25) by adding the ordinal value of the letter (97-122) to the key and subtracting 97, before taking the remainder of that value. For instance, 'a' shifted 1 would be -> (97 + 1 - 97) % 26 = 1.
  - Then, add the remainder to 97 to get the new letter. 'a' shifted by 1 would require adding 1 to 97, which yields 98 ('b').

**Big O:**
- O(n) time
  - loops through each letter in the string; linear time.
- O(n) space
  - new string with length n is initialized.