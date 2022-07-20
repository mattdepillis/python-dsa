---
Problem: Non-Constructible Change
Type: Array
Date Written: 07-19-2022
---

# Problem
Given an array of positive values representing the values of coins in your possession, write a function that returns the minimum amount of change that you cannot create. Coin values must be positive and don't have to be unique.

For example, python```nonconstructible_change([1, 2, 5])``` should return ```4```.

# Solution
I first take the sum of the array and add one to create the current minimum possible change that could be returned if the current array elements don't cover all possible combinations of values up to their collective sum. For example, python```[1, 1, 1]``` would return 4 because the array elements can cover 1-3, 3 being the sum of all elements. I then sort the elements because I want to have similar-sized elements next to each other - problems can be introduced to this solution if a 4 is next to a 1, while there's a 2 later on in the array (my algorithm may suggest that change of 3 cannot be made in this instance).

I then loop through each number from 1 to ```current_min_sum``` to see if each value is covered by the change in array. To do this, I set python```counter = i```; counter allows me to see whether or not array values can reduce the counter value to 0, meaning that that number of change is covered. For example, in the second top loop of python```[1, 1, 1]```, counter=2 will be reduced to 0 after 2nd loop since subtracting 1 and 1 from 2 = 0.

If at any point in the second for-loop counter has been reduced to 0, I break the loop and start on the next min-change number to evaluate. Else, if the array has been traversed and the counter is still a positive number, we know that change has not been met for that value and thus it is returned as minimum change.

If all numbers in the range are successfully evaluated, return the original minimum possible change: the sum of all array elements + 1.

**Pseudocode:**
- set ```current_min_change``` to python```sum(array) + 1```.
- sort the array.
- loop over all the possible values to assess from 1 to the sum of the array.
- for each value to assess:
  - set a counter as value against which array elements can be subtracted, to see whether or not the array can make change for this value.
  - loop through the array elements. for each element:
    - if the value to assess - the element >= 0, make that subtraction.
    - if the counter is now zero, break and start a new value to assess.
  - if the loop ends and the counter is a positive number, return it.
- else, return the original determined value for minimum change: array's sum + 1.

**Big O:**
- O(n * sum) time
  - in the worst case, this algorithm would have to traverse through n array elements for every value from 1 to sum.
- O(sum) space
  - the initialization of counter in each loop means a new value is stored into memory for each iteration of the first for-loop.

**Assessment of this approach:**
It's not a terrible solution - it's decently fast and is a logical way to tackle this problem. Small change values that can't be covered will actually be resolved quite fast with this algorithm. It probably wouldn't scale very well to large arrays that contain a first missing sum at a much higher number value (say, 1000), although that's likely an edge case for an algorithm like this -- you're likely to find a value of missing change earlier on unless the array is huge and has balanced values.

Nonetheless, there's a better one-loop solution that works conceptually and runs faster on larger arrays.

# Revised Solution, and Why it Improves on the First
We can instead devise a one-pass solution to the problem that's quicker. Here's the logic: sort the array, set a minimum_change to 0, and start looping over each value. If a given value is greater than the minimum_change + 1, break the loop and return the value. Else, add that element to the given minimum_change value.

Why this makes conceptual sense: let's say I have an array python```[1, 2, 3, 4]```. The first loop will run fine because python```1 > minimum_change + 1``` evaluates to False, and 1 is added to minimum_change. The same works for the second loop - 2 isn't greater than 1+ 1, and because of that we know we can make change of 2 -- this is the value of the element itself. The same would be true if the second element was 1: 1 > 2.

But if we had an array python```[1, 3, 4]```, the second loop through would ensure that we cannot make change of 2, since 3 > minimum_change + 1 = 2.

**Pseudocode:**
- sort the array.
- for each element in the array:
  - if it's larger than python```minimum_change + 1```, break the loop.
  - else, add it to minimum_sum.
- return minimum_sum + 1 -- the +1 ensures we return the higher of the array sum + 1, or the current value of change we had + 1 (the min change we cannot make from array values).

**Big O:**
- O(n) time
  - Looping through the array takes O(n) time. All operations within the loop are time-constant.
- O(1) space
  - No additional space is used other than that of the initialized variables.