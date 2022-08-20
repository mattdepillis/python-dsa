---
Problem: Find 3 Largest Numbers
Type: Search
Date Written: 08-17-2022
---

# Problem
Write a function that takes in an array of >= 3 ints and, without sorting the input array, returns a sorted array of the three largest integers in the input array.

For example, python```find_three_largest_nums([10, 5, 9, 10, 12])``` should return ```[10, 10, 12]```.

# Solution
I was a little confused by the categorization of the question, and was pressed for time so did not write out a full in-place shift method.

Instead, while the list size is greater than 3, I take the min of the first 4 values and remove it from the array.

**Pseudocode:**
- while the length of the list is greater than 3,
  - remove the smallest integer of the first 4 list items.
- return the list, sorted.

**Big O:**
- O(n^2) time
  - in this case, we run 2 O(n) operations inside the while-loop, which itself trends towards executing ~ n times. Not great.
- O(1) space
  - we're performing operations on the same array - no new vars declared.

**Problems with this approach:**
- It could be more efficient. O(n^2) time complexity is awful, despite the concise code.

# A Better Solution
Instead, we can make use of two tricks to write a better algorithm:
- we can init an fixed-size array full of negative infinite values to start, which takes case of the negative number case.
- sorting a fixed-size array within a loop is an O(1) operation because the time complexity doesn't change with an increase in n - therefore, we can do so within a loop without performance degradation.

**Pseudocode:**
- init an array of size 4 ```largest``` to contain all ```-inf``` values.
- for each number in the array:
  - set ```largest[0]``` equal to number.
  - sort the array.
- return ```largest[-3:]``` - the largest 3 nums left in the largest array (at the back of the array after sort).

**Big O:**
- O(n) time
  - we iterate through each array element once. sorting the constant-size array is an O(1) operation inside a loop. 
- O(1) space  
  - the size of the return array ```largest``` is consistent across input sizes.