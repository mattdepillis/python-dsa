"""
Given a binary tree to search and a target node, find the target node's successor if traversing the tree in order (l -> root -> r).

TC: worst-case O(n)
SC: O(h) -- worst-case, need to store h recursive calls on the stack. variable space consistent at each level
"""
import sys
from os import path

sys.path.append(path.dirname( path.dirname ( path.dirname ( path.abspath(__file__) ) ) ))

from ae_bst import Tree as t


def inorder_traversal(node, node_to_find, last_visited, successor):
  if successor: return (last_visited, successor)

  if node.left:
    (last_visited, successor) = inorder_traversal(node.left, node_to_find, last_visited, successor)

  if node:
    if last_visited == node_to_find: successor = node
    last_visited = node
  if node.right:
    (last_visited, successor) = inorder_traversal(node.right, node_to_find, last_visited, successor)

  return last_visited, successor


def find_successor(tree, node):
  return inorder_traversal(tree, node, last_visited=None, successor=None)


if __name__ == "__main__":
  tree = t()
  nodes = [
    {"id": "1", "left": "2", "parent": None, "right": "3", "value": 1},
    {"id": "2", "left": "4", "parent": "1", "right": "5", "value": 2},
    {"id": "3", "left": None, "parent": "1", "right": None, "value": 3},
    {"id": "4", "left": "6", "parent": "2", "right": None, "value": 4},
    {"id": "5", "left": None, "parent": "2", "right": None, "value": 5},
    {"id": "6", "left": None, "parent": "4", "right": None, "value": 6}
  ]

  for node in nodes:
    tree.insert_node(tree.root, node)

  # NOTE: for sake of time, this will not be tested locally as new functions would need to be written.
  # this problem was solved on ae console.