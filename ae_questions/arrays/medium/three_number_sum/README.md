---
Problem: Three Number Sum
Type: Array
Date Written: 08-19-2022
---

# Problem
Write a function that takes in an array of distinct integers and a target sum, and returns all the possible combinations of three numbers that sum to the target sum as an array of arrays. Make sure that child arrays are sorted smallest to largest, and that the parent array is as well.

For example, python```three_number_sum([12, 3, 1, 2, -6, 5, -8, 6], 0)``` should return ```[[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]```.

# Solution
I used a double for-loop and a dictionary to keep track of diffs from the target value, as well as current pairs. The top loop loops through each integer until it reaches the n - 2 number, while the second for-loop pairs each sequential each integer with the top-loop anchor value. 

**Pseudocode:**
- init a results array that will hold the subarrays of 3 values that sum to python```target```.
- loop through each value in the array as an anchor value, until the n-2 element. because we're looping in order to create pairs to compare to a third value, we don't need to loop through python```array[len(n) - 2]``` and python```array[len(n) - 1]``` -- they don't have 2 sequential array elements to form a 3.
  - init a dict to track combinations for the anchor index.
  - for each following index j in the array (python```range(i + 1, len(array))```):
    - check if the value at that index is a key in the dictionary. if it is:
      - append it to the values array at that key.
      - append that values array, sorted, to the results dictionary.
    - take the sum of array[i] and array[j] and subtract it from the target value, and save it in a variable ```diff```. diff is the number we'd need to add to this pairing of values to equal the target value. This step takes care of direction -- for example, if target = 0 and we have values array ```[2, 3]```, we'll produce a diff of ```0 - 5 = -5```.
    - set python```dict[diff] = [values]```.
- return the results array, sorted. this ensures that the subarrays are properly sorted by value (for example, ```[-8, 3, 5]``` might be added before ```[-8, 2, 6]```, but the latter is lesser than the former due to the smaller middle value).

**Big O:**
- O(n^2) time
  - time complexity trends toward n^2 time because we're nesting for-loops. In practice, it will be less than n^2 since the second loop shrinks in items to iterate through for each increment of the top loop. For notation purposes, n^2 is most accurate. all operations inside the loops themselves are constant-time.
- O(n) space
  - each iteration, a dict is created and released. it has maximum storage requirements in proportion to n.