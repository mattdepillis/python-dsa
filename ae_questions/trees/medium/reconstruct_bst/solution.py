"""
Given a non-empty array of ints representing the order in which a tree's nodes would be visited in a preorder traversal algorithm, write a function that inserts the nodes into a tree accoringly and returns the tree.

TC: O(n) -- iterate through the nodes array
SC: O(n) -- must create a tree with n nodes
"""

# Node class
class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

# places each node into its correct place in the tree
def place_node(tree, node):
  if node < tree.value:
    if tree.left: place_node(tree.left, node)
    else: tree.left = Node(node)
  else:
    if tree.right: place_node(tree.right, node)
    else: tree.right = Node(node)

  return tree

# preorder traversal algorithm to check work
def preorder_traversal(node, list):
  if node: list.append(node.value)
  if node.left: preorder_traversal(node.left, list)
  if node.right: preorder_traversal(node.right, list)
  return list

# reconstruct bst function
def reconstruct_bst(nodes):
  tree = Node(nodes[0])
  for node in nodes[1:]:
    place_node(tree, node)
  return tree


if __name__ == "__main__":
  print(reconstruct_bst([10, 4, 2, 1, 5, 17, 19, 18]))