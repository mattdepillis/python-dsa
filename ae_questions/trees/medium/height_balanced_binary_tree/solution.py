"""
Given the root of a binary tree, return True if the BT is height-balanced, and False if it isn't.

A BT is height balanced if, at any given node of the tree, its left and right subtrees have a depth difference of greater than 1.

TC: O(n) -- worst-case, must reach each node in the tree.
SC: O(d), where d = max depth. Must hold maximum of d recursive calls on the stack at a time.
"""
import sys
from os import path

sys.path.append(path.dirname( path.dirname ( path.dirname ( path.abspath(__file__) ) ) ))

from ae_bst import Tree as t


def find_depths_at_node(node, balanced):
  max_left = max_right = 0

  if node.left:
    ml, bl = find_depths_at_node(node.left, balanced)
    if not bl: return (0, False)
    max_left += 1 + ml
  if node.right:
    hr, br = find_depths_at_node(node.right, balanced)
    if not br: return (0, False)
    max_right += 1 + hr

  if abs(max_left - max_right) > 1:
    balanced = False

  return max(max_left, max_right), balanced


def height_balanced_binary_tree(node):
  return find_depths_at_node(node, balanced=True)[1]


if __name__ == "__main__":
  nodes = [
    {"id": "1", "left": "2", "right": "3", "value": 1},
    {"id": "2", "left": "4", "right": "5", "value": 2},
    {"id": "3", "left": None, "right": "6", "value": 3},
    {"id": "4", "left": None, "right": None, "value": 4},
    {"id": "5", "left": "7", "right": "8", "value": 5},
    {"id": "6", "left": None, "right": None, "value": 6},
    {"id": "7", "left": None, "right": None, "value": 7},
    {"id": "8", "left": None, "right": None, "value": 8}
  ]

  tree = t()

  for node in nodes:
    tree.insert_node(tree.root, node)

  # print(tree.preorder_traversal(tree.root, list=[]))
  print(height_balanced_binary_tree(tree.root))