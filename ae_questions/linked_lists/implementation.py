class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def insert(self, data):
    value = data["value"]
    new_node = Node(value)

    if self.head is None:
      self.head = new_node
    else:
      current = self.head
      while current.next is not None:
        current = current.next
      current.next = new_node
    

  def traverse(self):
    current = self.head

    while current is not None:
      print(current.value)
      current = current.next