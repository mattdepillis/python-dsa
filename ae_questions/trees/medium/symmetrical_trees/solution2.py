"""
Write a function that takes in a binary tree and determines whether or not it's symmetrical.
"""
import sys
from os import path

sys.path.append(path.dirname( path.dirname ( path.dirname ( path.abspath(__file__) ) ) ))

from ae_bst import Tree as t


def inorder_traversal(node, list):
  if node.left: inorder_traversal(node.left, list)
  if node: list.append(node.value)
  if node.right: inorder_traversal(node.right, list)
  return list

def is_symmetrical_tree(tree):
  left, right = [tree.left], [tree.right]

  while len(left) > 0:
    l, r = left.pop(0), right.pop(0)
    if not l and not r: continue
    
    if (l and r) and l.value == r.value:
      left = left + [l.left, l.right]
      right = right + [r.right, r.left]
    else: return False

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