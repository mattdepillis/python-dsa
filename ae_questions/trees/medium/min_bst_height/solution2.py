"""
Provided a non-empty sorted array of integers, write a function that constructs a BST of minimal height.

TC: O(n) -- traversing through each node provided in the array
SC: O(n) -- new node (bst) obj for each item in array. More space-efficient, as no new arrays are created (this solution updates indices, which is better from SC perspective).
"""

# test BST (Node) class
class BST:
  def __init__(self, value):
    self.root = None
    self.value = value
    self.left = None
    self.right = None

  # node insertion method
  def insert(self, current, value):
    if value < current.value:
      if not current.left:
        current.left = BST(value)
      else: self.insert(current.left, value)
    else:
      if not current.right:
        current.right = BST(value)
      else: self.insert(current.right, value)


# preorder traversal method (node -> left -> right)
def preorder_traversal(current, list):
  if current:
    list.append(current.value)
  if current.left:
    preorder_traversal(current.left, list)
  if current.right:
    preorder_traversal(current.right, list)

  return list

# min_bst_height helper function -- set the middle num as the current node
def place_middle(array, start, end):
  if start > end: return None
  middle_index = (start + end) // 2
  
  tree = BST(array[middle_index])
  tree.left = place_middle(array, start, middle_index - 1)
  tree.right = place_middle(array, middle_index + 1, end)

  return tree


def min_bst_height(array):
  tree = place_middle(array, 0, len(array) - 1)
  print(preorder_traversal(tree, []))
  return tree


if __name__ == "__main__":

  print(min_bst_height(
    [1, 2, 5, 7, 10, 13, 14, 15, 22] # root = Node(10)
  ))

  # print(min_bst_height(
  #   [1] # root = Node(1)
  # ))

  # print(min_bst_height(
  #   [1, 2, 5, 7] # root = Node(2) / Node(5)
  # ))

  # print(min_bst_height(
  #   [1, 2, 5, 7, 10, 13, 14, 15] # root = Node(7) / Node(10)
  # ))
