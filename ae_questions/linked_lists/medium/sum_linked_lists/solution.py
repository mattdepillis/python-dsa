"""
Given two linked lists both storing a value from 0-9 at each node, calculate the combined sum of the two lists. Construct and return a new linked list that represents the combined sum. Each node traversed in a linkedlist should represent a jump in the 10s place.

For example, ```sum_linked_lists()``` on list1 = 0 -> 9 -> 1 and list2 = 2 -> 1 -> 2 should return a linked list of 2 -> 0 -> 4.  
"""
import sys
from os import path

sys.path.append(path.dirname( path.dirname ( path.dirname ( path.abspath(__file__) ) ) ))

from implementation_for_local import LinkedList

def helper(list):
  current, sum = list.head, ''
  while current:
    sum = str(current.value) + sum
    current = current.next
  return int(sum)

def sum_linked_lists(list1, list2):
  sum = helper(list1) + helper(list2)
  split = list(str(sum))
  composite = LinkedList()
  for s in split[::-1]:
    composite.simple_insert_at_end(int(s))

  return composite


if __name__ == "__main__":
  list1, list2 = LinkedList(), LinkedList()
  for n in [2, 4, 7, 1]:
    list1.simple_insert_at_end(n)
  for m in [9, 4, 5]:
    list2.simple_insert_at_end(m)

  c = sum_linked_lists(list1, list2)
  c.traverse()
