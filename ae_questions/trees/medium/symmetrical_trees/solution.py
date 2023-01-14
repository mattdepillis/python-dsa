"""
Write a function that takes in a binary tree and determines whether or not it's symmetrical.

TC: O(n), where n = nodes
SC: O(n + d), where n = nodes (values stored in list) and d = max depth of tree (max calls on stack)
"""
import sys
from os import path

sys.path.append(path.dirname( path.dirname ( path.dirname ( path.abspath(__file__) ) ) ))

from ae_bst import Tree as t

# helper function -- performs inorder_traversal on the tree
def inorder_traversal(node, list):
  if node.left: inorder_traversal(node.left, list)
  if node: list.append(node.value)
  if node.right: inorder_traversal(node.right, list)
  return list

# inorder traversal, then confirm that the returned list is "palindromic"
def is_symmetrical_tree(tree):
  iot = inorder_traversal(tree, list=[])

  i, j = 0, len(iot) - 1

  while i < j:
    if iot[i] != iot[j]: return False
    i, j = i + 1, j - 1

  return True


if __name__ == "__main__":
  tree = t()

  nodes = [
    {"id": "1", "left": "2", "right": "2-2", "value": 1},
    {"id": "2", "left": "3", "right": "3-2", "value": 2},
    {"id": "2-2", "left": "3-3", "right": "3-4", "value": 2},
    {"id": "3", "left": None, "right": None, "value": 3},
    {"id": "3-2", "left": None, "right": None, "value": 3},
    {"id": "3-3", "left": None, "right": None, "value": 3},
    {"id": "3-4", "left": None, "right": None, "value": 3}
  ]

  for node in nodes:
    tree.insert_node(tree.root, node)

  # print(tree.preorder_traversal(tree.root, list=[]))
  print(is_symmetrical_tree(tree.root))