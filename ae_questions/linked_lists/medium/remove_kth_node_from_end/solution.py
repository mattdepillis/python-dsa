"""
Remove kth node from end of the LinkedList class.
"""
import sys
from os import path

sys.path.append(path.dirname( path.dirname ( path.dirname ( path.abspath(__file__) ) ) ))

from implementation_for_local import LinkedList

def remove_kth_node_from_end(list, k):
  counter = 0
  first = second = list.head
  while first:
    counter += 1
    first = first.next

  c = counter - k
  if c == 0:
    list.head = list.head.next
    return list
  while c > 1:
    c -= 1
    second = second.next
  second.next = second.next.next

  return list

if __name__ == "__main__":
  list = LinkedList()
  for item in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    list.simple_insert_at_end(item)

  list = remove_kth_node_from_end(list, 8)

  list.traverse()