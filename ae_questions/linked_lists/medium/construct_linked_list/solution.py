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
    return node if node else Node(value)

  """
  creates a node, regardless of whether there's currently a node in the list with the same value.
  """
  def createNode(self, value):
    return Node(value)

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
    if not self.head:
      self.head = self.tail = node
      return
    return self.insertBefore(self.head, node)

  """
  sets the passed-through value as the linked list's tail node.
  moves an already-existing node to the tail position, rather than creating a new node with the same value.
  """
  def setTail(self, node):
    if not self.tail:
      self.head = self.tail = node
      return
    return self.insertAfter(self.tail, node)
  
  """
  inserts nodeToInsert into the list before node.
  if nodeToInsert is already in the list, it's first removed.
  then the method inserts it in front of node, taking into account whether or not node is self.head.
  """
  def insertBefore(self, node, nodeToInsert):
    if nodeToInsert.prev or nodeToInsert.next:
      nodeToInsert = self.remove(nodeToInsert)

    if not node.prev:
      self.head = nodeToInsert
    else:
      node.prev.next = nodeToInsert

    nodeToInsert.prev, nodeToInsert.next, node.prev = node.prev, node, nodeToInsert

  """
  inserts nodeToInsert into the list after node.
  if nodeToInsert is already in the list, it's first removed.
  then the method inserts it after node, taking into account whether or not node is self.tail.
  """
  def insertAfter(self, node, nodeToInsert):
    if nodeToInsert.prev or nodeToInsert.next:
      nodeToInsert = self.remove(nodeToInsert)

    if not node.next:
      self.tail = nodeToInsert
    else:
      node.next.prev = nodeToInsert

    nodeToInsert.prev, nodeToInsert.next, node.next = node, node.next, nodeToInsert

  """
  """
  def insertAtPosition(self, position, nodeToInsert):
    current, position = self.head, position - 1
    print(current)
    while position > 0:
      current, position = current.next, position - 1
    
    return self.insertBefore(current, nodeToInsert)

  """
  """
  def removeNodesWithValue(self, value):
    current = self.head
    while current:
      if current.value == value:
        curr = current.next if current.next else current
        self.remove(current)
        current = curr
      current = current.next

  """
  """
  def remove(self, node):
    prev, next = node.prev, node.next
    if not prev:
      self.head, next.prev = next, None
      return
    if not next:
      self.tail, prev.next = prev, None
      return
    else:
      prev.next, next.prev = next, prev
    node.prev = node.next = None
    return node


if __name__ == "__main__":
  # create a new linked list
  list = DoublyLinkedList()

  # insert nodes into list with list.setHead()
  # nodes = [1, 2, 3, 4, 5]
  # for n in nodes[::-1]:
  #   list.setHead(list.createOrReturnNode(n))

  # * test setHead for already-existing node in DoublyLinkedList.
  # list.setHead(list.createOrReturnNode(4))
  # * test insertBefore for a non-head edge case.
  # node = list.createOrReturnNode(4)
  # node2 = list.createOrReturnNode(3)
  # list.insertBefore(node2, node)
  # * test setTail for already-existing node in DoublyLinkedList.
  # node = list.createOrReturnNode(3)
  # list.setTail(node)
  # * test insertAfter for a non-tail edge case.
  # node = list.createOrReturnNode(3)
  # node2 = list.createOrReturnNode(4)
  # list.insertAfter(node2, node)
  # * test removeNodesWithValue. This tests an edge case (tail).
  # list.setTail(list.createNode(3))
  # list.removeNodesWithValue(3)
  # * test insertAtPosition.
  # list.insertAtPosition(1, list.createNode(6))
  # * testing -- case 1
  # nodes = [1, 2, 3, 4, 5]
  # for n in nodes[::-1]:
  #   list.setHead(list.createOrReturnNode(n))
  # list.setHead(list.createOrReturnNode(4))
  # list.setTail(list.createNode(6))
  # list.insertBefore(list.createOrReturnNode(6), list.createOrReturnNode(3))
  # list.insertAfter(list.createOrReturnNode(6), list.createNode(3))
  # list.insertAtPosition(1, list.createNode(3))
  # list.removeNodesWithValue(3)
  # list.remove(list.createOrReturnNode(2))
  # * testing -- case 2
  # nodes = [1]
  # for n in nodes:
  #   list.setHead(list.createOrReturnNode(n))
  # * testing -- case 3
  # nodes = [1]
  # for n in nodes:
  #   list.setTail(list.createOrReturnNode(n))
  # * testing -- case 17
  # list.setHead(list.createOrReturnNode(1))
  # list.insertAfter(list.createOrReturnNode(1), list.createOrReturnNode(2))
  # list.insertAfter(list.createOrReturnNode(2), list.createOrReturnNode(3))
  # list.remove(list.createOrReturnNode(1))
  # * testing -- case 16
  list.setHead(list.createOrReturnNode(1))
  list.removeNodesWithValue(1)

  list.traverse_forward()
  print('--------------')
  list.traverse_backward()