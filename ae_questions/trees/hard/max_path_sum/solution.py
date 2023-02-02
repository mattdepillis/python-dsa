"""
Write a function that takes a binary tree and returns its max path sum, which is a one-directional path of connected nodes in the tree.

TC: O(n) -- traverse every node in the tree
SC: O(log(n)) -- at most, you'll have log(n) recursive calls on the stack
  - this is because, at a depth of 3 in a balanced binary tree (7 total nodes, for example), you'd have max 3 recursive calls on the stack at a given time. 3 ~= (approaches) log2(7).
"""
import sys
from os import path

sys.path.append(path.dirname( path.dirname ( path.dirname ( path.abspath(__file__) ) ) ))

from ae_bst import Tree as t

def recurse(tree, levels):
  cont = iso = tree.value
  if not tree.left and not tree.right: return [cont, iso]
  left = right = [float('-inf'), float('-inf')]
  if tree.left: left = recurse(tree.left, levels + 1)
  if tree.right: right = recurse(tree.right, levels + 1)

  cont += max(left[0], right[0]) if not levels == 0 else left[0] + right[0]
  iso = max(
    left[1],
    right[1],
    left[0] + right[0] + tree.value,
    tree.value,
    left[0] + tree.value,
    right[0] + tree.value
  )

  return [cont, iso]

def max_path_sum(tree):
  return max(recurse(tree, 0))


if __name__ == "__main__":
  tree = t()

  # nodes = [
  #   {"id": "1", "left": "2", "right": "3", "value": 1},
  #   {"id": "3", "left": "6", "right": "7", "value": 3},
  #   {"id": "7", "left": None, "right": None, "value": 7},
  #   {"id": "6", "left": None, "right": None, "value": 6},
  #   {"id": "2", "left": "4", "right": "5", "value": 2},
  #   {"id": "5", "left": None, "right": None, "value": 5},
  #   {"id": "4", "left": None, "right": None, "value": 4}
  # ]

  # nodes = [
  #   {"id": "1", "left": "2", "right": "-1", "value": 1},
  #   {"id": "-1", "left": None, "right": None, "value": -1},
  #   {"id": "2", "left": None, "right": None, "value": 2}
  # ]

  # nodes = [
  #   {"id": "1", "left": "-5", "right": "3", "value": 1},
  #   {"id": "3", "left": None, "right": None, "value": 3},
  #   {"id": "-5", "left": "6", "right": None, "value": -5},
  #   {"id": "6", "left": None, "right": None, "value": 6}
  # ]

  # nodes = [
  #   {"id": "-2", "left": "-1", "right": None, "value": -2},
  #   {"id": "-1", "left": "2", "right": "3", "value": -1},
  #   {"id": "2", "left": None, "right": None, "value": 2},
  #   {"id": "3", "left": None, "right": None, "value": 3}
  # ]

  nodes = [
    {"id": "2", "left": "-3", "right": "1", "value": 2},
    {"id": "-3", "left": "6", "right": "5", "value": -3},
    {"id": "6", "left": None, "right": "7", "value": 6},
    {"id": "5", "left": None, "right": None, "value": 5},
    {"id": "7", "left": None, "right": None, "value": 7},
    {"id": "1", "left": None, "right": None, "value": 1}
  ]

  for node in nodes:
    tree.insert_node(tree.root, node)

  # print(tree.preorder_traversal(tree.root, list=[]))
  print(max_path_sum(tree.root))