---
Problem: Run-Length Encoding
Type: String
Date Written: 08-09-2022
---

# Problem
Write a function that takes a string and and returns its run-length encoding. Run-length encoding is a form of lossless data compression in which runs (or streaks) of data are stored in a single value and count. Runs of 10+ should be split into multiple runs.

For example, python```run_length_encoding('AAA')``` should return ```'3A```, and python```run_length_encoding(AAAAAAAAAAAA)``` should return 9A3A.

# Solution
My first solution was clunky and didn't have enough consolidated logic. For example, the final if-statement could be executed before the return every invocation and didn't need to be inside an if-statement.

The major hit to brevity: the need to keep track of 2 vars (count and char) to append something to the encoding string at the end. We'll see how an array changes that.

# A Better Solution
Instead, the second solution uses an array to keep track of the current char. If the current element doesn't equal the array's last item or the array length is too long, simply calculate the length of the array and append it + the array's first character to the encoded string. Else, the array can just be overwritten with the new value.

The benefit of using an array in this approach - you don't need to store 2 vars to track count and character... just append to array and manage these at case failure.

**Pseudocode:**
- initialize an empty string to hold the transformed encoding.
- initialize python```current``` as an array of length 1, containing the first element of the string.
- iterate through the rest of the string indices:
  - if the char at a string index is equal to the last element in the current array, AND the length of the current array is less than 9, add the char to the array.
  - else, add python```f"{len(current)}{current[0]}``` to the string and set current equal to [i].
- On the last element (loop is broken), add python```f"{len(current)}{current[0]}``` to the string.
- return the string.

**Big O:**
- O(n) time
  - have to loop through all string indices - operations within loop mostly time-constant or close to it (with Pythonic array append operation being the potential caveat).
- O(n) space
  - new string is initialized - in worst case, could be double length of string but will stay directly proportional.