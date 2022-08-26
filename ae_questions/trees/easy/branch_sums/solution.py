"""
Write a function that takes in a binary tree's root node and returns an array containing the sums of all the paths in the tree.
"""
######## IMPORTS ########
import sys
from os import path

# adds 2nd parent dir to path so that implementation's LinkedList class can be accessed
sys.path.append( path.dirname( path.dirname ( path.dirname ( path.abspath(__file__) ) ) ) )

from bst import Tree
######## END IMPORTS ########

def branch_sums(node, sums, branch_sum=0):
  branch_sum += node.value
  if node.left:
    branch_sums(node.left, sums, branch_sum)
  if node.right:
    branch_sums(node.right, sums, branch_sum)
  if not node.left and not node.right:
    sums.append(branch_sum)

  return sums 


if __name__ == "__main__":
  # init a tree instance and add nodes.
  tree = Tree(10)
  nodes = [5, 13, 4, 16, 12, 7]
  for node in nodes:
    tree.insert_node(tree.root, node)

  # ? should expect branch sums for above nodes of [19, 22, 35, 39]
  print(branch_sums(tree.root, sums=[]))