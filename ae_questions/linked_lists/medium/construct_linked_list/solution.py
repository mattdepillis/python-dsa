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

  TC: O(1), SC: O(1)
  """
  def setHead(self, node):
    if not self.head:
      self.head = self.tail = node
      return
    return self.insertBefore(self.head, node)

  """
  sets the passed-through value as the linked list's tail node.
  moves an already-existing node to the tail position, rather than creating a new node with the same value.

  TC: O(1), SC: O(1)
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

  TC: O(1), SC: O(1)
  """
  def insertBefore(self, node, nodeToInsert):
    if nodeToInsert.prev or nodeToInsert.next:
      self.remove(nodeToInsert)

    if not node.prev:
      self.head = nodeToInsert
    else:
      node.prev.next = nodeToInsert

    nodeToInsert.prev, nodeToInsert.next, node.prev = node.prev, node, nodeToInsert

  """
  inserts nodeToInsert into the list after node.
  if nodeToInsert is already in the list, it's first removed.
  then the method inserts it after node, taking into account whether or not node is self.tail.

  TC: O(1), SC: O(1)
  """
  def insertAfter(self, node, nodeToInsert):
    if nodeToInsert.prev or nodeToInsert.next:
      self.remove(nodeToInsert)

    if not node.next:
      self.tail = nodeToInsert
    else:
      node.next.prev = nodeToInsert

    nodeToInsert.prev, nodeToInsert.next, node.next = node, node.next, nodeToInsert

  """
  inserts a node at a given position in the linked list (self.head = 1).
  if head is none, set the node as the head node.
  else, iterate through the list by decrementing position until the desired position is reached.
  then, insert the node before the node that's already there.

  TC: O(p) where p = position, SC: O(1)
  """
  def insertAtPosition(self, position, nodeToInsert):
    if self.head is None:
      return self.setHead(nodeToInsert)
    current, position = self.head, position - 1
    while position > 0:
      current, position = current.next, position - 1
    
    return self.insertBefore(current, nodeToInsert)

  """
  removes all nodes with specified value from the list.
  starts with the list head.
  moves current to next. if the previous node (on rep 1, would be list.head), has value, remove it.

  TC: O(n), SC: O(1)
  """
  def removeNodesWithValue(self, value):
    current = self.head
    while current:
      current, prev = current.next, current
      if prev.value == value:
        self.remove(prev)

  """
  removes a node from the doubly linked list.
  checks 1) that it's not both head and tail, 2) that it's not either. If so, handles adjacents accordingly.
  else, connects previous and following nodes.
  finally, sets own prev and next to None to disconnect from list.

  TC: O(1), SC: O(1)
  """
  def remove(self, node):
    prev, next = node.prev, node.next
    if not prev and not next:
      self.head = self.tail = None
    elif not prev:
      self.head, next.prev = next, None
    elif not next:
      self.tail, prev.next = prev, None
    else:
      prev.next, next.prev = next, prev
    node.prev = node.next = None


if __name__ == "__main__":
  # create a new linked list
  list = DoublyLinkedList()

  # insert nodes into list with list.setHead()
  # nodes = [1, 2, 3, 4, 5]
  # for n in nodes[::-1]:
  #   list.setHead(list.createOrReturnNode(n))
  # list.setTail(list.createOrReturnNode(1))

  for i in range(4):
    list.setHead(list.createNode(1))
  list.removeNodesWithValue(1)

  list.traverse_forward()
  print('--------------')
  list.traverse_backward()