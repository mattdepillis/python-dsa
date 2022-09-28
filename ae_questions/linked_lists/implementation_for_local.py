"""
Simple linked list implementation. only inserts at end at the moment.
Allows items to be added by data of just an int, rather than via object (like AE does).
Will be modified to contain more specific insertion methods for more complex linked list problems.
"""

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None


class LinkedList:
  def __init__(self):
    self.head = None

  # insertion at end of the linked list, assuming each new node will be added to the end of the list
  # ? used in: easy -> remove duplicates from linked list
  def simple_insert_at_end(self, value):
    new_node = Node(value)

    if self.head is None:
      self.head = new_node
    else:
      current = self.head
      while current.next is not None:
        current = current.next
      current.next = new_node    

  # standard linked list traversal function.
  # traverses through the nodes and prints value at each position
  def traverse(self):
    current = self.head

    while current is not None:
      print(current.value)
      current = current.next