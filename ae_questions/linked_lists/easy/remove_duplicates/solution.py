"""
Given the head of a singly-linked list whose nodes are sorted in order by value, write a function that returns the list with the duplicate values removed.
"""
######## IMPORTS ########
import sys
from os import path

# adds 2nd parent dir to path so that implementation's LinkedList class can be accessed
sys.path.append( path.dirname( path.dirname ( path.dirname ( path.abspath(__file__) ) ) ) )

from implementation_for_ae import LinkedList
######## END IMPORTS ########

# creates a list from a JSON-imported linked list format
def create_list(nodes):
  linked_list = LinkedList()
  for node in nodes:
    linked_list.simple_insert_at_end(node)
  return linked_list

# remove duplicates function
def remove_duplicates_from_linked_list(list):
  linked_list = create_list(list["nodes"])

  current = linked_list.head
  while current.next is not None:
    advance = False

    next = current.next
    while not advance:
      if next is None or next.value != current.value:
        advance = True
      else:
        next = next.next
        current.next = next
    if current.next is not None:
      current = current.next
  
  # linked_list.traverse()
  return linked_list


if __name__ == "__main__":
  list = {
    "nodes": [
      {"id": "1", "next": "9", "value": 1},
      {"id": "9", "next": "11", "value": 9},
      {"id": "11", "next": "15", "value": 11},
      {"id": "15", "next": "15-2", "value": 15},
      {"id": "15-2", "next": "16", "value": 15},
      {"id": "16", "next": "17", "value": 16},
      {"id": "17", "next": "17-2", "value": 17},
      {"id": "17-2", "next": None, "value": 17}
    ]
  }
  remove_duplicates_from_linked_list(list)