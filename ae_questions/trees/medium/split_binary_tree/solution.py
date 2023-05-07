"""
Given a binary tree with at least one node, write a function that determines whether or not that binary tree could be split into 2 trees of equal total value by removing an edge.
Return the split sum if this is possible. If not, return 0.

TC: O(n) -- must iterate through all nodes once to get total sum, and then once to figure out whether or not tree can be split.
SC: O(d) -- proportional to the depth of the tree, as recurse() will have max d recursive calls on the stack at a given time.
"""
class BinaryTree:
  """ Binary tree node class. """
  def __init__(self, value, left=None, right=None):
      self.value = value
      self.left = left
      self.right = right

def construct_local_tree(nodes):
  """ Constructs a tree from a list of node objects. Returns the tree root"""
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
  """ Recursively finds the total sum of the tree, starting from root. """
  if node.left: sum = find_total_tree_sum(node.left, sum)
  if node.right: sum = find_total_tree_sum(node.right, sum)

  return sum + node.value

def can_split_at_node(value, value_children, total_sum):
  """ Determines whether or not a node and the sum of its cumulative children could form a split tree. """
  return value + value_children == .5 * total_sum


def recurse(node, tree_sum):
  """
  Recurses down the tree to find a given node at which the tree could be split.
  If ```split``` is True from a call to children, just returns those values.
  Else, will determine whether or not this node could be included in a split.
  """
  child_sum_left = child_sum_right = 0

  if node.left:
    split, split_value, child_sum_left = recurse(node.left, tree_sum)
    if split: return split, split_value, child_sum_left
  if node.right:
    split, split_value, child_sum_right = recurse(node.right, tree_sum)
    if split: return split, split_value, child_sum_right
  
  if can_split_at_node(node.value, child_sum_left, tree_sum):
    return True, child_sum_left + node.value, child_sum_left + node.value
  if can_split_at_node(node.value, child_sum_right, tree_sum):
    return True, child_sum_right + node.value, child_sum_left + node.value
  if can_split_at_node(node.value, sum([child_sum_left, child_sum_right]), tree_sum):
    s = sum([child_sum_left, child_sum_right]) + node.value
    return True, s, s

  return False, None, child_sum_left + child_sum_right + node.value


def split_binary_tree(tree):
  """ Handler method - finds sum and split_sum through helper functions. """
  sum = find_total_tree_sum(tree, 0)
  split_sum = recurse(tree, sum)
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
  # nodes = [
  #   {"id": "1", "left": "9", "right": "20", "value": 1},
  #   {"id": "9", "left": "5", "right": "2", "value": 9},
  #   {"id": "20", "left": "30", "right": "10", "value": 20},
  #   {"id": "30", "left": None, "right": None, "value": 30},
  #   {"id": "10", "left": "35", "right": "25", "value": 10},
  #   {"id": "35", "left": None, "right": None, "value": 35},
  #   {"id": "25", "left": None, "right": None, "value": 25},
  #   {"id": "5", "left": None, "right": None, "value": 5},
  #   {"id": "2", "left": "3", "right": None, "value": 2},
  #   {"id": "3", "left": None, "right": None, "value": 3}
  # ]

  root = construct_local_tree(nodes)
  split_sum = split_binary_tree(root)
  print(split_sum)