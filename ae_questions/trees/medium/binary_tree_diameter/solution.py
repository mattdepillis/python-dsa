"""
Write a function that takes in a binary tree and returns its diameter, which is defined as the length of its longest path (doesn't have to include the root).

TC: O(n) -- each node is visited once
SC: O(d) -- the number of recursive calls stored on the stack is directly proportional to the max height of the tree, d.
"""
import sys
from os import path

sys.path.append(path.dirname( path.dirname ( path.dirname ( path.abspath(__file__) ) ) ))

from ae_bst import Tree as t

def helper(node, list):
  max_left = max_right = 0

  if node.left:
    max_left = helper(node.left, list)

  if node.right:
    max_right = helper(node.right, list)
  
  list.append(max_left + max_right)

  return max(max_left + 1, max_right + 1)


def binary_tree_diameter(root):
  list = []
  helper(root, list)
  return max(list)


if __name__ == "__main__":
  tree = t()

  # nodes = [
  #   {"id": "1", "left": "3", "right": "2", "value": 1},
  #   {"id": "3", "left": "7", "right": "4", "value": 3},
  #   {"id": "7", "left": "8", "right": None, "value": 7},
  #   {"id": "8", "left": "9", "right": None, "value": 8},
  #   {"id": "9", "left": None, "right": None, "value": 9},
  #   {"id": "4", "left": None, "right": "5", "value": 4},
  #   {"id": "5", "left": None, "right": "6", "value": 5},
  #   {"id": "6", "left": None, "right": None, "value": 6},
  #   {"id": "2", "left": None, "right": None, "value": 2}
  # ]

  nodes = [
    {"id": "1", "left": "2", "right": "3", "value": 1},
    {"id": "3", "left": "6", "right": "7", "value": 3},
    {"id": "7", "left": None, "right": None, "value": 7},
    {"id": "6", "left": None, "right": None, "value": 6},
    {"id": "2", "left": "4", "right": "5", "value": 2},
    {"id": "5", "left": None, "right": None, "value": 5},
    {"id": "4", "left": None, "right": None, "value": 4}
  ]

  for node in nodes:
    tree.insert_node(tree.root, node)

  print(binary_tree_diameter(tree.root))

  # print(tree.preorder_traversal(tree.root, list=[]))