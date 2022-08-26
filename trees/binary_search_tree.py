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


if __name__ == "__main__":
  # 3 is a low number; this will be a very lopsided tree (most nodes on the right).
  # tree = Tree(3)
  # nodes = [1, 5, 2, 4, 6, 8, 7, 12, 9, 10, 11]

  # tree = Tree(10)
  # nodes = [5, 11, 13, 4, 7, 6, 3, 12, 8, 2, 1, 15, 14, 20]

  tree = Tree(13)
  nodes = [5, 4, 3, 6, 7, 23, 22, 28, 32, 27]

  for node in nodes:
    tree.insert_node(tree.root, node)
  
  # print(tree.preorder_traversal(tree.root, list=[]))
  # print(tree.inorder_traversal(tree.root, list=[]))
  print(tree.postorder_traversal(tree.root, list=[]))