"""
Given the head of a singly-linked list whose nodes are sorted in order by value, write a function that returns the list with the duplicate values removed.
"""
import sys
from os import path

# adds 2nd parent dir to path so that implementation's LinkedList class can be accessed
sys.path.append( path.dirname( path.dirname ( path.dirname ( path.abspath(__file__) ) ) ) )

from implementation import LinkedList

def remove_duplicates_from_linked_list(list):
  linked_list = LinkedList()
  for node in list["nodes"]:
    linked_list.insert(node)
  linked_list.traverse()    

if __name__ == "__main__":
  list = {
    "nodes": [
      {"id": "1", "next": "9", "value": 1},
      {"id": "9", "next": "11", "value": 9},
      {"id": "11", "next": "15", "value": 11},
      {"id": "15", "next": "15-2", "value": 15},
      {"id": "15-2", "next": "16", "value": 15},
      {"id": "16", "next": "17", "value": 16},
      {"id": "17", "next": None, "value": 17}
    ]
  }
  remove_duplicates_from_linked_list(list)