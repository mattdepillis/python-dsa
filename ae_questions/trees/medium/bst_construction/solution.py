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

  def preorder_traversal(self, node, list):
    if node:
      list.append(node.value)
    if node.left:
      self.preorder_traversal(node.left, list)
    if node.right:
      self.preorder_traversal(node.right, list)

    return list

  def inorder_traversal(self, node, list):
    if node.left:
      self.postorder_traversal(node.left, list)
    if node:
      list.append(node.value)
    if node.right:
      self.postorder_traversal(node.right, list)
    return list

  def postorder_traversal(self, node, list):
    if node.left:
      self.postorder_traversal(node.left, list)
    if node.right:
      self.postorder_traversal(node.right, list)
    if node:
      list.append(node.value)

    return list

  def remove(self, node, value):
    if not node:
      return node
    elif value > node.value:
      node.right = self.remove(node.right, value)
    elif value < node.value:
      node.left = self.remove(node.left, value)
    else:
      if not node.right:
        return node.left
      if not node.left:
        return node.right
      
      start = node.right
      while start.left:
        start = start.left
      start.left, start.right = node.left, node.right
      node = start
      return node
    return node


if __name__ == "__main__":
  bst = BST(10)
  to_insert = [5, 15, 2, 6, 1, 13, 22, 12, 14]
  for item in to_insert:
    bst.insert(item, bst.root)

  print(bst.preorder_traversal(node=bst.root, list=[]))

  node = bst.remove(node=bst.root, value=2)

  print(bst.preorder_traversal(node=bst.root, list=[]))
  # print(bst.inorder_traversal(node=bst.root, list=[]))
  # print(bst.postorder_traversal(node=bst.root, list=[]))
  # print(bst.contains(10, bst.root))