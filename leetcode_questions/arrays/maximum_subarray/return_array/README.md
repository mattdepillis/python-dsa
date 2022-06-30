---
Problem: Maximum Subarray - Return Array
Type: Array
Date Written: 06-29-2022
---

# Problem
Given an array of integers, return the subarray whose values sum to the greatest number. This problem is closely related to the Maximum Subarray - Return Sum question, except it requires an array, not an integer, as a return value.

For example, python```maximum_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])``` should return ```[4, -1, 2, 1]```. ```python maximum_subarray([1, -2, 2, 3, 4, -2, 3])``` should return ```[2, 3, 4, -2, 3]```.

# Solution
**The key elements to solving this problem:**
- keeping track of start and end indices.
- comparing a running sum of the elements in question to a maximum sum total.

**Pseudocode:**
- start by setting start and end indices to 0.
- start by setting ```current_sum```, the sum of all the indices we're counting, and ```max_sum```, the maximum sum for a subarray within the nums array, to 0.
- iterate over each array element by index.
- add each array element to the ```current_sum``` variable to tally overall subarray sum. ```current_sum``` now equals itself + the element ```nums[i]```.
- if a given array value ```nums[i]``` is greater than both ```current_sum``` (e.g. the total sum of the subarray, itself included) and ```max_sum```, ```current_sum``` and ```max_sum``` are reset to ```nums[i]```, effectively discarding the array indices that came before and restarting the subarray count. set ```start = i``` and ```end = i + 1``` to lock the element in as the current maximum_subarray by itself.
- else if ```current_sum >= max_sum```, the max should include this array index. we shift the end index to include this number in the max_subarray, and set the max subarray's value equal to the current total value.
- do nothing if ```current_sum < max_sum```; if, say ```[2, 3, 4, -2]``` is our array, we don't want to add -2 to the maximum subarray because its inclusion would mean we don't have the maximum possible subarray value.
- once we've looped through the array elements in O(n) time, return the array from the start to end (+1 since the end indice is exclusive) indices.

**Big O:**
- O(n) time
  - have to loop through each array element
- O(1) space
  - storing values for a set number of variables: max and current sum, start and end indices