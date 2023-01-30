"""

"""
class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

def place_node(tree, node):
  # if not tree: tree = Node(node)
  if node < tree.value:
    if tree.left: place_node(tree.left, node)
    else: tree.left = Node(node)
  else:
    if tree.right: place_node(tree.right, node)
    else: tree.right = Node(node)

  return tree


def preorder_traversal(node, list):
  if node: list.append(node.value)
  if node.left: preorder_traversal(node.left, list)
  if node.right: preorder_traversal(node.right, list)
  return list


def reconstruct_bst(nodes):
  tree = Node(nodes[0])
  for node in nodes[1:]:
    place_node(tree, node)

  l = preorder_traversal(tree, list=[])
  print(l)
  return tree


if __name__ == "__main__":
  print(reconstruct_bst([10, 4, 2, 1, 5, 17, 19, 18]))