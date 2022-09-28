"""
Given the head of a singly-linked list whose nodes are sorted in order by value, write a function that returns the list with the duplicate values removed.
"""
######## IMPORTS ########
import sys
from os import path

# adds 2nd parent dir to path so that implementation's LinkedList class can be accessed
sys.path.append( path.dirname( path.dirname ( path.dirname ( path.abspath(__file__) ) ) ) )

from solution import create_list
######## END IMPORTS ########

def remove_duplicates_from_linked_list(list):
  linked_list = create_list(list["nodes"])

  current = linked_list.head
  while current.next is not None:
    if current.value == current.next.value:
      current.next = current.next.next
    else:
      current = current.next
  
  linked_list.traverse()
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
