"""
Implementation of a binary search tree for initial understanding and practice.
"""
class Node:
  def __init__(self, id, value, left, right):
    self.id = id
    self.value = value
    self.left = left
    self.right = right


class Tree:
  def __init__(self):
    self.root = None

  """
  """
  def dfs_to_find_value(self, node, id):
    if node.left:
      if isinstance(node.left, str):
        if node.left == id:
          return (node, 'left')
      else:
        n = self.dfs_to_find_value(node.left, id)
        if n:
          return n

    if node.right:
      if isinstance(node.right, str):
        if node.right == id:
          return (node, 'right')
      else:
        return self.dfs_to_find_value(node.right, id)
  
  """
  """
  def insert_node(self, current, node):
    new_node = Node(node['id'], node['value'], node['left'], node['right'])

    if not current:
      self.root = new_node
    else:
      (parent, side) = self.dfs_to_find_value(self.root, node['id'])
      if side == 'left':
        parent.left = new_node
      elif side == 'right':
        parent.right = new_node

    return

  """
  inorder traversal method.
    traverses left -> root -> right.
  """
  def inorder_traversal(self, node, list):
    return list
    
  """
  preorder traversal method.
    traverses root -> left -> right.
  """
  def preorder_traversal(self, node, list):
    list.append(node.value)
    if node.left and not isinstance(node.left, str):
      self.preorder_traversal(node.left, list)
    if node.right and not isinstance(node.right, str):
      self.preorder_traversal(node.right, list)
    return list

  """
  postorder traversal method.
    traverses the tree left -> right -> root.
  """
  def postorder_traversal(self, node, list):
    return list