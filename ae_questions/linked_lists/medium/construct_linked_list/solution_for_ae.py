"""
Construct a doubly-linked list.
"""

class Node:
  def __init__(self, value):
    self.value = value
    self.prev = None
    self.next = None

class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  # add node
  def insert_at_end(self, value):
    node = Node(value)
    if self.head is None:
      self.head = node
    else:
      current = self.head
      while current.next is not None:
        current = current.next
      current.next = node
      node.prev = current
      self.tail = node

  # traverseForward
  def traverse_forward(self):
    current = self.head
    while current is not None:
      print(current.value)
      current = current.next

  # traverse backward
  def traverse_backward(self):
    current = self.tail
    while current is not None:
      print(current.value)
      current = current.prev

  # setHead (insert at beginning) -- self, node
  def setHead(self, node):
    if self.head is None:
      self.head = self.tail = node
      return
    node.next, self.head.prev = self.head, node

  # insertAfter(self, node, nodeToInsert)
  # insertAtPosition(self, position, nodeToInsert)
  # removeNodesWithValue(self, value)
  # remove(self, node)
  # containsNodeWithValue(self, value)
  def containsNodeWithValue(self, value):
    current = self.head
    while current is not None:
      if current.value == value:
        return current
      current = current.next

if __name__ == "__main__":
  list = DoublyLinkedList()
  nodes = [
    {"id": "1", "next": None, "prev": None, "value": 1},
    {"id": "2", "next": None, "prev": None, "value": 2},
    {"id": "3", "next": None, "prev": None, "value": 3},
    {"id": "3-2", "next": None, "prev": None, "value": 3},
    {"id": "3-3", "next": None, "prev": None, "value": 3},
    {"id": "4", "next": None, "prev": None, "value": 4},
    {"id": "5", "next": None, "prev": None, "value": 5},
    {"id": "6", "next": None, "prev": None, "value": 6}
]
  for node in filter(lambda x: x["value"] < 6 and len(x["id"]) == 1, nodes):
    list.setHead(node)
  
  list.traverse_forward()
  # list.traverse_backward()
  # print(list.containsNodeWithValue(4))