"""
Write in a function that takes in a binary tree's root and a target value, and returns the node value closest to the target value.
"""
import sys
from os import path
sys.path.append( path.dirname ( path.dirname ( path.dirname ( path.abspath(__file__) ) ) ) )
from bst import Tree

def find_closest_value(node, target, closest):
  if node is None:
    return closest
  
  diff = target - node.value
  if diff == 0:
    return node.value
  if closest is None or abs(diff) < abs(target - closest):
    closest = node.value
  return find_closest_value(node.left, target, closest) if diff < 0 else find_closest_value(node.right, target, closest)


if __name__ == "__main__":
  tree = Tree(10)
  nodes = [5, 13, 4, 16, 12, 7]
  for node in nodes:
    tree.insert_node(tree.root, node)

  print(find_closest_value(tree.root, 8, closest=None))
