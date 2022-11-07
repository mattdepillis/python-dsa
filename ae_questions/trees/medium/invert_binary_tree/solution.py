"""
Write a function that inverts a binary tree -- that is, the function should swap each left node in the tree with its corresponding right node.

TC: O(n) -- need an operation on each node in the tree
SC: O(d), where d = max depth of the tree -- this is because we need to store a number of recursive calls on the stack proportional to d at a given time
"""
import sys
from os import path

sys.path.append(path.dirname( path.dirname ( path.dirname ( path.abspath(__file__) ) ) ))

from ae_bst import Tree as t


def invert_binary_tree(node):
  node.left, node.right = node.right, node.left

  if node.left:
    invert_binary_tree(node.left)
  if node.right:
    invert_binary_tree(node.right)


if __name__ == "__main__":
  tree = t()
  nodes = [
    {"id": "1", "left": "2", "right": "3", "value": 1},
    {"id": "2", "left": "4", "right": "5", "value": 2},
    {"id": "3", "left": "6", "right": "7", "value": 3},
    {"id": "4", "left": "8", "right": "9", "value": 4},
    {"id": "5", "left": None, "right": None, "value": 5},
    {"id": "6", "left": None, "right": None, "value": 6},
    {"id": "7", "left": None, "right": None, "value": 7},
    {"id": "8", "left": None, "right": None, "value": 8},
    {"id": "9", "left": None, "right": None, "value": 9}
  ]

  for node in nodes:
    tree.insert_node(tree.root, node)

  print(tree.preorder_traversal(tree.root, list=[]))
  invert_binary_tree(tree.root)
  print(tree.preorder_traversal(tree.root, list=[]))