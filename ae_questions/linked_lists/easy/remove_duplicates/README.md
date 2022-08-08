---
Problem: Remove Duplicates from Linked List
Type: Linked List
Date Written: 08-05-2022
---

# Problem
Given the head of a singly-linked list whose nodes are sorted in order by value, write a function that returns the list with the duplicate values removed.

For example, python```remove_duplicates_from_linked_list()``` should return ```5```.

# Solution
My original solution uses a while loop to traverse through the linked list's nodes. At each node in the list, it looks forward to see whether the value of the next node is None or not equal to the value of the current node - if this is the case, it'll step along to the next node. Else, it sets the current node's next to ```next.next```. Once the traversal is complete, it returns the modified linked list.

**Pseudocode:**
- create the linked list.
- set python```current = linked_list.head``` to access the first node.
- while python```current.next``` isn't none:
  - set a boolean flag "advance" that will allow us to exit the nested while loop if the next value is none or unequal.
  - while advance is False,
    - check if we can exit the loop.
    - else, set the value of current.next = current.next.next.
  - check that current.next isn't none - if it isn't, then go to the next node.

**Big O:**
- O(n) time
  - the time the algorithm takes to run is directly proportional to the time complexity of linked list traversal - O(n).
- O(1) space
  - The algorithm uses the same amount of space regardless of size n.

**Issues With this Approach:**
- The implementation works and reaches the fastest possible time complexity for this problem (due to linked list traversal Big O), but is written in a klutzy manner. The code can be refined to become simpler, more readable, and elegant.
- The fact that the algorithm can advance to multiple nodes within the top-level while loop makes it necessary to repeat python```if current.next is not None```, which elongates the solution and is repetitive.

# Revised Solution, and Why it Improves on the First
Use the same top-level while loop to traverse through the linked list nodes. However, we shorten the code by asserting that if python```current.value == current.next.value```, then set python```current.next = current.next.next```. Otherwise, just set current = current.next and move along the list.

**Big O:**
- O(n) time
- O(n) space