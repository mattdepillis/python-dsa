---
Problem: Validate Subsequence
Type: Array
Date Written: 07-05-2022
---

# Problem
Given two non-empty arrays of integers, determine whether the second is a valid subsequence of the first. A valid subsequence means the numbers in the sequence must all appear in the exact same order in the array.

For example, python```validate_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10])``` should return ```True```.

# Solution
I initially chose to loop through each number in the sequence, each time determining whether the number existed in the sequence. If it did, I'd overwrite the array as python```array = array[index + 1 :]``` so as to cut the array off after the index. This would prevent numbers reversed in the index from the sequence from being detected. If the number went unfound in the array, False would be returned. 

**Pseudocode:**
- loop through sequence.
- for each number in sequence, try finding the index of that number in the array.
- if found, set the array as python```array = array[index + 1 :]``` and rerun the loop.
- else, catch the ValueError and return False.
- if made to the end of the loop, return True.

**Big O:**
- O(n*m) time
  - You have to loop through n items in ```sequence``` and m items for each ```array``` index search.
- O(1) space
  - Space is constant because you're simply resetting the array with new values in memory after each index find operation.

**Issues With this Approach:**
- n*m time complexity isn't great -- the killer operation in this solution is python```array.index()```. This is an O(n) operation within a loop.
- we could simplify the solution to use constant-time operations within the for-loop.

# Revised Solution, and Why it Improves on the First
The two-pointer approach -- one for the sequence and one for the array -- is a quicker method.

**Pseudocode:**
- create a pointer for ```sequence``` and set it equal to 0. This value will be used to traverse the sequence array.
- loop through the array. ```i``` acts as the traversal pointer for ```array```.
- at each index of the array,
  - if the sequence pointer ```j``` is greater than the length of the sequence, that means that all sequence items have been traversed (this index is out of array scope). break the loop.
  - else if ```i``` equals ```sequence[j]```, the current pointer for array matches the value of the pointer index in sequence. Increment ```j``` by 1.
- at the end of the loop, we know that the subsequence is valid if ```len(sequence)``` is equal to ```j```, and invalid if not. For example, python```validate_subsequence([5, 1, 22, 25, -1, 6, 8, 10, -1], [1, 6, -1, -1])``` would return false because j would get stuck at 3 -- ```j``` wouldn't increment for the -1 placed in front of the 6.

**Big O:**
- O(n) time
  - Looping through the array takes O(n) time. All operations within the loop are time-constant.
- O(1) space
  - No additional space is used other than that of the initialized variables.