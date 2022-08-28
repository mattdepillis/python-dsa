"""
Write a function that takes a binary tree and returns the total sum of its root node's depths.
"""
import sys
from os import path
sys.path.append( path.dirname ( path.dirname ( path.dirname ( path.abspath(__file__) ) ) ) )
from bst import Tree

def node_depths(node, depth):
  if node is None:
    return 0
  return depth + node_depths(node.left, depth + 1) + node_depths(node.right, depth + 1)

if __name__ == "__main__":
  tree = Tree(10)
  nodes = [5, 13, 4, 16, 12, 7]
  for node in nodes:
    tree.insert_node(tree.root, node)

  print(node_depths(tree.root, depth=0))