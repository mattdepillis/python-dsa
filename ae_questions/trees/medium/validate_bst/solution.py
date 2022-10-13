"""
Write a function that takes a BST and returns a boolean value signifying whether it's valid. A BST is valid if, at any node in the tree, a right child is greater and a left child is lesser. (For purposes of this question, can be greater/less than or equal to).
"""
import sys
from os import path

sys.path.append(path.dirname( path.dirname ( path.dirname ( path.abspath(__file__) ) ) ))

from bst import Tree

def validate_bst(node):
  if node.left:
    if node.left.value > node.value:
      return False
    validate_bst(node.left)
  if node.right:
    if node.right.value < node.value:
      return False
    validate_bst(node.right)

  return True

if __name__ == "__main__":
  tree = Tree(10)
  for item in [5, 15, 2, 6, 1, 13, 22, 14]:
    tree.insert_node(tree.root, item)
  print(tree.preorder_traversal(tree.root, list=[]))

  print(validate_bst(tree.root))