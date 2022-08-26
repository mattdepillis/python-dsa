"""
Implementation of a binary search tree for initial understanding and practice.
"""
class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class Tree:
  def __init__(self, value):
    self.root = Node(value)
 
  """
  insert a node into the tree.
    compares the value of the current node with the value to insert.
    current.value > value means the node will be inserted on the left of this current node, or in current.left's children.
    current.value < value means the node will be inserted on the right of this current node, or in current.right's children.
  """
  def insert_node(self, current, value):
    if current.value > value:
      if not current.left:
        current.left = Node(value)
      else:
        self.insert_node(current.left, value)
    elif current.value < value:
      if not current.right:
        current.right = Node(value)
      else:
        self.insert_node(current.right, value)
    else:
      return

  """
  inorder traversal method.
    traverses left -> root -> right.
  """
  def inorder_traversal(self, node, list):
    if node.left:
      self.inorder_traversal(node.left, list)
    if node:
      list.append(node.value)
    if node.right:
      self.inorder_traversal(node.right, list)
    return list
    
  """
  preorder traversal method.
    traverses root -> left -> right.
  """
  def preorder_traversal(self, node, list):
    if node:
      list.append(node.value)
    if node.left:
      self.preorder_traversal(node.left, list)
    if node.right:
      self.preorder_traversal(node.right, list)

    return list

  """
  postorder traversal method.
    traverses the tree left -> right -> root.
  """
  def postorder_traversal(self, node, list):
    if node.left:
      self.postorder_traversal(node.left, list)
    if node.right:
      self.postorder_traversal(node.right, list)
    if node:
      list.append(node.value)

    return list