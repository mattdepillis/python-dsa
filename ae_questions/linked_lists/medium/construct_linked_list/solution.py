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

  ### * HELPER FUNCTIONS * ###

  """
  traverses the doubly-linked list forward.
  TC: O(n), SC: O(1)
  """
  def traverse_forward(self):
    current = self.head
    while current is not None:
      print(current.value)
      current = current.next

  """
  traverses the doubly-linked list backward.
  TC: O(n), SC: O(1)
  """
  def traverse_backward(self):
    current = self.tail
    while current is not None:
      print(current.value)
      current = current.prev

  """
  determines whether a node in the list exists with the passed-through value.
  this function likely replicates AE's behind-the-scenes node discovery function that keeps other methods constant time-complex.
  TC: O(n), SC: O(1)
  """
  def createOrReturnNode(self, value):
    node = self.containsNodeWithValue(value)
    if not node:
      node = Node(value)
    return node

  ### ! END HELPER FUNCTIONS ! ###
  ### * FUNCTIONS TO CONSTRUCT * ###

  """
  returns the list node containing a given value.
  TC: O(n), SC: O(1)
  """
  def containsNodeWithValue(self, value):
    current = self.head
    while current is not None:
      if current.value == value:
        return current
      current = current.next
    return None

  """
  sets the passed-through value as the linked list's head node.
  moves an already-existing node to the head position, rather than creating a new node with the same value.
  """
  def setHead(self, node):
    # print('n', node)
    if self.head is None:
      self.head = self.tail = node
      return
    # TODO: modify to return value from insertBefore
    node.next, self.head.prev = self.head, node
    self.head = node

  """
  """
  def setTail(self, node):
    return node
  
  """
  """
  def insertBefore(self, node, nodeToInsert):
    return node

  """
  """
  def insertAfter(self, node, nodeToInsert):
    return node

  """
  """
  def insertAtPosition(self, position, nodeToInsert):
    return node

  """
  """
  def removeNodesWithValue(self, value):
    return node

  """
  """
  def remove(self, node):
    return node


if __name__ == "__main__":
  # create a new linked list
  list = DoublyLinkedList()

  # insert nodes into list with list.setHead()
  nodes = [1, 2, 3, 4, 5]
  for n in nodes[::-1]:
    node = list.createOrReturnNode(n)
    list.setHead(node)

  list.traverse_forward()
  print('--------------')
  list.traverse_backward()
  
  # testing additional operations
  # node = list.createOrReturnNode(4)
  # list.setHead(node)