"""
Construct a basic BST implementation with insert, remove and contain methods. Note - calling bst.remove() on a single-node tree should not delete the element.
"""
class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BST:
  def __init__(self, value):
    self.root = Node(value)

  def insert(self, value, node):
    if value > node.value:
      if not node.right:
        node.right = Node(value)
      else:
        self.insert(value, node.right)
    elif value < node.value:
      if not node.left:
        node.left = Node(value)
      else:
        self.insert(value, node.left)
    else:
      return

  def contains(self, value, node):
    if not node:
      return False
    elif node.value == value:
      return True
    elif node.value > value:
      return self.contains(value, node.left)
    elif node.value < value:
      return self.contains(value, node.right)
    

  def preorder_traversal(self, node):
    if not node:
      return
    else:
      print(node.value)
      self.preorder_traversal(node.left)
      self.preorder_traversal(node.right)


if __name__ == "__main__":
  bst = BST(8)
  to_insert = [6, 4, 7, 10]
  for item in to_insert:
    bst.insert(item, bst.root)

  bst.preorder_traversal(node=bst.root)
  print(bst.contains(10, bst.root))