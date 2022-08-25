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
  preorder traversal method.
    starts with root node, traverses all the way left, then makes its way right across the tree.
  """
  def preorder_traversal(self, node, list):
    if node:
      list.append(node.value)
      if node.left:
        self.preorder_traversal(node.left, list)
      if node.right:
        self.preorder_traversal(node.right, list)

    return list


if __name__ == "__main__":
  # 3 is a low number; this will be a very lopsided tree (most nodes on the right).
  tree = Tree(3)
  nodes = [1, 5, 2, 4, 6, 8, 7, 12, 9, 10, 11]
  for node in nodes:
    tree.insert_node(tree.root, node)
  
  print(tree.preorder_traversal(tree.root, list=[]))