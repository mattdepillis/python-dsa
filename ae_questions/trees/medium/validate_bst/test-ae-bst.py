"""
"""
import sys
from os import path

sys.path.append(path.dirname( path.dirname ( path.dirname ( path.abspath(__file__) ) ) ))

from ae_bst import Tree

if __name__ == "__main__":
  tree = Tree()

  nodes = [
    {"id": "10", "left": "5", "right": "15", "value": 10},
    {"id": "15", "left": None, "right": "22", "value": 15},
    {"id": "22", "left": None, "right": None, "value": 22},
    {"id": "5", "left": "2", "right": "5-2", "value": 5},
    {"id": "5-2", "left": None, "right": "11", "value": 5},
    {"id": "11", "left": None, "right": None, "value": 11},
    {"id": "2", "left": "1", "right": None, "value": 2},
    {"id": "1", "left": None, "right": None, "value": 1}
  ]
  for node in nodes:
    tree.insert_node(tree.root, node)

  print(tree.preorder_traversal(tree.root, list=[]))