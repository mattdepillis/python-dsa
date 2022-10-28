"""
Write a function that takes a BST and returns a boolean value signifying whether it's valid. A BST is valid if, at any node in the tree, a right child is greater and a left child is lesser. (For purposes of this question, can be greater/less than or equal to).

***Solution2 improves upon Solution1 by proposing a simpler solution than adding a prior node to ```less``` when traversing right or ```greater``` when traversing left, and then calculating the minimum greater value + maximum lesser value to compare to.***

***Instead, this solution first sets ```min = float('-inf')``` and ```max = float('inf')``` when starting tree traversal at the root. When traversing right at each level, it replaces the prior value of min with the value of the prior node. When traversing left, it replaces max with the prior node's value.***

TC: O(n) -- all tree nodes are traversed to confirm validity in the worst case
SC: O(d) -- space used will be proportional to the max depth of the tree (as each recursive call must be added to stack for execution)
"""
import sys
from os import path

sys.path.append(path.dirname( path.dirname ( path.dirname ( path.abspath(__file__) ) ) ))

from ae_bst import Tree as t

def validate_bst_children(node, min, max):
  if not node:
    return True
  if node.value < min or node.value >= max:
    return False

  if not validate_bst_children(node.left, min, node.value):
    return False
  return validate_bst_children(node.right, node.value, max)

def validate_bst(root):
  return validate_bst_children(root, float('-inf'), float('inf'))

if __name__ == "__main__":
  tree = t()

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