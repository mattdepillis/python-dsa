"""
Write a function that takes a BST and a positive integer k, and returns the kth largest value in the BST. Duplicate integers should be treated as different values. Return -1 if not found.

TC: O(h + k) -- need to traverse down h levels to begin reverse traversal, and then must add k elements to the array before returning the kth element.
SC: O(h) -- have up to h-proportional recursive calls on the stack at max, as the traversal needs to (at the very least) start at the greatest value (which could be located at max depth)
"""
import sys
from os import path

sys.path.append(path.dirname( path.dirname ( path.dirname ( path.abspath(__file__) ) ) ))

from ae_bst import Tree as t

def reverse_traversal(node, list, k):
  if node.right:
    f = reverse_traversal(node.right, list, k)
    if isinstance(f, int): return f

  list.append(node.value)
  if len(list) == k:
    return list[k - 1]

  if node.left:
    f = reverse_traversal(node.left, list, k)
    if isinstance(f, int): return f

  return list

def kth_largest_value(tree, k):
  return reverse_traversal(tree, [], k)


if __name__ == "__main__":
  tree = t()

  nodes = [
    {"id": "15", "left": "5", "right": "20", "value": 15},
    {"id": "20", "left": "17", "right": "22", "value": 20},
    {"id": "22", "left": None, "right": None, "value": 22},
    {"id": "17", "left": None, "right": None, "value": 17},
    {"id": "5", "left": "2", "right": "5-2", "value": 5},
    {"id": "5-2", "left": None, "right": None, "value": 5},
    {"id": "2", "left": "1", "right": "3", "value": 2},
    {"id": "3", "left": None, "right": None, "value": 3},
    {"id": "1", "left": None, "right": None, "value": 1}
  ]

  # nodes = [
  #   {"id": "5", "left": "4", "right": "6", "value": 5},
  #   {"id": "4", "left": "3", "right": None, "value": 4},
  #   {"id": "6", "left": None, "right": "7", "value": 6},
  #   {"id": "7", "left": None, "right": None, "value": 7},
  #   {"id": "3", "left": None, "right": None, "value": 3}
  # ]

  for node in nodes:
    tree.insert_node(tree.root, node)

  print(kth_largest_value(tree.root, 3))