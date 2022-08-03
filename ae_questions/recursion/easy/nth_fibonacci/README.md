---
Problem: Nth Fibonacci
Type: Recursion
Date Written: 07-21-2022
---

# Problem
Write a function that takes the number n and returns the nth fibonacci number recursively.

This implementation asks the author to count 0 as the first number in the sequence; as a note, I've seen other definitions of this problem in which 1 was regarded the first num, so this solution may vary slightly from others.

sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...

For example, python```nth_fibonacci(6)``` should return ```5```.

# Solution
If you treat the number 0 as the first number of the sequence, you want to return the value ```n-1``` for any n less than or equal to zero. This means that python```nth_fibonacci(1)``` would return n - 1 = 0, and python```nth_fibonacci(2)``` would return n-1 = 1.

For any value of n greater than 2, the algorithm returns python```nth_fibonacci(n - 1) + nth_fibonacci(n - 2)```. This recursively calls the function again at smaller values, until the base case execution is reached (0 or 1). This recursive method creates a recursive tree; for example, python```nth_fibonacci(3)``` can be broken down into python```nth_fibonacci(2) + nth_fibonacci(1)```, adding an extra layer of executions to the stack.

**Pseudocode:**
- if the value of n is less than or greater to 2, return n - 1.
- else, recursively call the function and add another layer of execution to the stack by returning the value as python```nth_fibonacci(n - 1) + nth_fibonacci(n - 2)```.

**Big O:**

**NOTE**: this is a complex discussion aided better with visual explanations and therefore the Notion page for this algorithm is a better place to conceptually review Big O.

- O(goldenratio^n) time
  - For each increment of n, we grow the depth of the recursive tree at a presumptive rate of goldenratio^n. the golden ratio is 1.618. Therefore, this is better than the oft-cited O(2^n) time complexity of this algorithm, but is nonetheless still exponential time.
- O(n) space
  - For each time the function has to go a level deeper on the recursive tree (e.g. to calculate python```nth_fibonacci(3)``` you must add python```nth_fibonacci(2)``` and python```nth_fibonacci(1)``` and evaluate them separately - since they both equal n - 1, they won't be on the stack at the same time). If we're trying to evaluate python```nth_fibonacci(3)``` and we first try to evaluate the child node python```nth_fibonacci(2)``` below it as well, the stack will have a depth of 2, taking up 2 memory slots in the stack. As n grows, the maximum depth of the recursive tree will approach n; therefore, the maximum amount of slots taken on the stack at any given time is linearly proportional to n.