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


def find_total_tree_sum(node, sum):
  if node.left: sum = find_total_tree_sum(node.left, sum)
  if node.right: sum = find_total_tree_sum(node.right, sum)

  return sum + node.value

def recurse(node, tree_sum, child_sum):
  if node.left:
    split, split_value, child_sum = recurse(node.left, tree_sum, child_sum)
    if split: return split, split_value, child_sum + node.value
  if node.right:
    split, split_value, child_sum = recurse(node.right, tree_sum, child_sum)
    if split: return split, split_value, child_sum + node.value
  
  if child_sum + node.value == .5 * tree_sum:
    return True, child_sum + node.value, child_sum + node.value
  return False, None, child_sum + node.value

def split_binary_tree(tree):
  sum = find_total_tree_sum(tree, 0)
  split_sum = recurse(tree, sum, 0)
  return split_sum[1] or 0


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
  split_sum = split_binary_tree(root)
  print(split_sum)