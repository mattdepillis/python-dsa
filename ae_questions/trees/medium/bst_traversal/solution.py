"""
Write preorder, inorder, and postorder traversal methods for a binary tree. Return a list of the node values for each method.

All 3 methods:
TC: O(n)
SC: O(n)
"""
import sys
from os import path

sys.path.append(path.dirname( path.dirname ( path.dirname ( path.abspath(__file__) ) ) ))

from ae_bst import Tree as t

"""
traverse the tree ```root -> left -> right```.
"""
def preorder_traversal(node, list):
  if node:
    list.append(node.value)
  if node.left:
    list = preorder_traversal(node.left, list)
  if node.right:
    list = preorder_traversal(node.right, list)
  return list

"""
traverse the tree ```left -> root -> right```.
"""
def inorder_traversal(node, list):
  if node.left:
    list = inorder_traversal(node.left, list)
  if node:
    list.append(node.value)
  if node.right:
    list = inorder_traversal(node.right, list)
  return list

"""
traverse the tree ```left -> right -> root```
"""
def postorder_traversal(node, list):
  if node.left:
    list = postorder_traversal(node.left, list)
  if node.right:
    list = postorder_traversal(node.right, list)
  if node:
    list.append(node.value)
  return list


if __name__ == "__main__":
  tree = t()

  """
  inorder = [1, 2, 5, 6, 10, 15, 22]
  preorder = [10, 5, 2, 1, 6, 15, 22]
  postorder = [1, 2, 6, 5, 22, 15, 10]
  """
  nodes = [
    {"id": "10", "left": "5", "right": "15", "value": 10},
    {"id": "15", "left": None, "right": "22", "value": 15},
    {"id": "22", "left": None, "right": None, "value": 22},
    {"id": "5", "left": "2", "right": "6", "value": 5},
    {"id": "6", "left": None, "right": None, "value": 6},
    {"id": "2", "left": "1", "right": None, "value": 2},
    {"id": "1", "left": None, "right": None, "value": 1}
  ]

  for node in nodes:
    tree.insert_node(tree.root, node)

  print(inorder_traversal(tree.root, list=[]))
  print(preorder_traversal(tree.root, list=[]))
  print(postorder_traversal(tree.root, list=[]))