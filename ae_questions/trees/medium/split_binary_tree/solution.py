"""

"""
class BinaryTree:
  """ Binary tree node class. """
  def __init__(self, value, left=None, right=None):
      self.value = value
      self.left = left
      self.right = right

def construct_local_tree(nodes):
  tree_nodes, root = {}, None
  for i in reversed(range(len(nodes))):
    node = nodes[i]
    val, left, right, id = node['value'], node['left'], node['right'], node['id']
    new_node = BinaryTree(
      val,
      tree_nodes[left] if left else left,
      tree_nodes[right] if right else right
    )
    if i == 0: root = new_node
    tree_nodes[id] = new_node
  return root

def find_total_tree_sum(tree):
  return tree

def split_binary_tree(tree):
  return tree


if __name__ == "__main__":
  """ Test Case 1 """

  nodes = [
    {"id": "1", "left": "2", "right": "3", "value": 1},
    {"id": "2", "left": "4", "right": "5", "value": 2},
    {"id": "3", "left": None, "right": "7", "value": 3},
    {"id": "4", "left": None, "right": None, "value": 4},
    {"id": "5", "left": None, "right": None, "value": 5},
    {"id": "7", "left": None, "right": None, "value": 7}
  ]

  root = construct_local_tree(nodes)