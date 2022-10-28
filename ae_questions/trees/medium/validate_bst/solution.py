"""
Write a function that takes a BST and returns a boolean value signifying whether it's valid. A BST is valid if, at any node in the tree, a right child is greater and a left child is lesser. (For purposes of this question, can be greater/less than or equal to).
"""
import sys
from os import path

sys.path.append(path.dirname( path.dirname ( path.dirname ( path.abspath(__file__) ) ) ))

from ae_bst import Tree as t

def validate_bst_children(node, less, greater):
  if node.value < max(less, default=float('-inf')) or node.value >= min(greater, default=float('inf')):
    return False
  else:
    if not node:
      return True
    valid = True
    if node.left:
      valid = validate_bst_children(node.left, less, greater + [node.value])
      if not valid:
        return False
    if node.right:
      valid = validate_bst_children(node.right, less + [node.value], greater)
    return valid

def validate_bst(root):
  if root.left:
    if not validate_bst_children(root.left, [], [root.value]):
      return False
  if root.right:
    if not validate_bst_children(root.right, [root.value], []):
      return False
  return True

if __name__ == "__main__":
  tree = t()

  # nodes = [ # ! 'False'
  #   {"id": "10", "left": "5", "right": "15", "value": 10},
  #   {"id": "15", "left": None, "right": "22", "value": 15},
  #   {"id": "22", "left": None, "right": None, "value": 22},
  #   {"id": "5", "left": "2", "right": "5-2", "value": 5},
  #   {"id": "5-2", "left": None, "right": "11", "value": 5},
  #   {"id": "11", "left": None, "right": None, "value": 11},
  #   {"id": "2", "left": "1", "right": None, "value": 2},
  #   {"id": "1", "left": None, "right": None, "value": 1}
  # ]

  # nodes = [ # ! 'True'
  #   {"id": "10", "left": "5", "right": "15", "value": 10},
  #   {"id": "15", "left": "13", "right": "22", "value": 15},
  #   {"id": "22", "left": None, "right": None, "value": 22},
  #   {"id": "13", "left": None, "right": "14", "value": 13},
  #   {"id": "14", "left": None, "right": None, "value": 14},
  #   {"id": "5", "left": "2", "right": "5-2", "value": 5},
  #   {"id": "5-2", "left": None, "right": None, "value": 5},
  #   {"id": "2", "left": "1", "right": None, "value": 2},
  #   {"id": "1", "left": None, "right": None, "value": 1}
  # ]

  # nodes = [ # ! 'False'
  #   {"id": "10", "left": "5", "right": "15", "value": 10},
  #   {"id": "15", "left": "13", "right": "22", "value": 15},
  #   {"id": "22", "left": None, "right": None, "value": 22},
  #   {"id": "13", "left": None, "right": "16", "value": 13},
  #   {"id": "16", "left": None, "right": None, "value": 16},
  #   {"id": "5", "left": "2", "right": "5-2", "value": 5},
  #   {"id": "5-2", "left": None, "right": None, "value": 5},
  #   {"id": "2", "left": "1", "right": None, "value": 2},
  #   {"id": "1", "left": None, "right": None, "value": 1}
  # ]

  # nodes = [ # ! 'True'
  #   {"id": "10", "left": "5", "right": "15", "value": 10},
  #   {"id": "15", "left": None, "right": "22", "value": 15},
  #   {"id": "22", "left": None, "right": None, "value": 22},
  #   {"id": "5", "left": "2", "right": "5-2", "value": 5},
  #   {"id": "5-2", "left": None, "right": None, "value": 5},
  #   {"id": "2", "left": "1", "right": None, "value": 2},
  #   {"id": "1", "left": "-5", "right": None, "value": 1},
  #   {"id": "-5", "left": "-15", "right": "-5-2", "value": -5},
  #   {"id": "-5-2", "left": None, "right": "-2", "value": -5},
  #   {"id": "-2", "left": None, "right": "-1", "value": -2},
  #   {"id": "-1", "left": None, "right": None, "value": -1},
  #   {"id": "-15", "left": "-22", "right": None, "value": -15},
  #   {"id": "-22", "left": None, "right": None, "value": -22}
  # ]

  nodes = [ # ! 'False'
    {"id": "10", "left": "5", "right": "15", "value": 10},
    {"id": "15", "left": None, "right": "22", "value": 15},
    {"id": "22", "left": None, "right": "500", "value": 22},
    {"id": "500", "left": "50", "right": "1500", "value": 500},
    {"id": "1500", "left": None, "right": "10000", "value": 1500},
    {"id": "10000", "left": "2200", "right": "9999", "value": 10000},
    {"id": "9999", "left": None, "right": None, "value": 9999},
    {"id": "2200", "left": None, "right": None, "value": 2200},
    {"id": "50", "left": None, "right": "200", "value": 50},
    {"id": "200", "left": None, "right": None, "value": 200},
    {"id": "5", "left": "2", "right": "5-2", "value": 5},
    {"id": "5-2", "left": None, "right": None, "value": 5},
    {"id": "2", "left": "1", "right": None, "value": 2},
    {"id": "1", "left": None, "right": None, "value": 1}
  ]

  for node in nodes:
    tree.insert_node(tree.root, node)
  print(tree.preorder_traversal(tree.root, list=[]))

  print(validate_bst(tree.root))