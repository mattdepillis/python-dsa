"""
Given the root node of a Binary Tree, a target node value to start from, and a value k, return all the nodes in the tree that are k edges away from the target node.

TC: O(n) -- store an adjacency graph for all nodes in the tree
SC: O(n) -- loop through all nodes in the tree
"""
class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

def map_relationships(node, node_value, parent_value, rels):
  """ Creates a hierarchical graph of parent-child relationships to be traversed. """
  entry = {
    "parent": parent_value, "children": []
  }

  if node.left: entry["children"].append(node.left)
  if node.right: entry["children"].append(node.right)

  for i, child in enumerate(entry["children"]):
    entry["children"][i] = child.value
    map_relationships(child, child.value, node.value, rels)
  rels[node_value] = entry

  return rels


def get_lower_nodes_distance_k(value, relationships, k_remaining):
  """ Gets nodes below current node that are distance k away. """
  entry = relationships[value]

  if k_remaining == 1: return entry["children"]
  lower_nodes_distance_k = []

  for child in entry["children"]:
    lower_nodes_distance_k += get_lower_nodes_distance_k(child, relationships, k_remaining - 1)

  return lower_nodes_distance_k


def get_upper_nodes_distance_k(value, visited, relationships, k, up):
  """
  Gets nodes above current node that are distance k away.
  NOTE: this method could probably be optimized. ****
  """
  if k == 1:
    nk = [child for child in relationships[value]['children'] if child not in visited]
    if relationships[value]['parent'] and up and relationships[value]['parent'] not in visited: nk += [relationships[value]['parent']]
    return nk

  upper_nodes_distance_k = []

  if relationships[value]['parent']:
    visited += [relationships[value]['parent']]
    upper_nodes_distance_k += get_upper_nodes_distance_k(relationships[value]['parent'], visited, relationships, k - 1, True)
  if k > 1:
    for child in relationships[value]['children']:
      if not child in visited:
        visited += [child]
        upper_nodes_distance_k += get_upper_nodes_distance_k(child, visited, relationships, k - 1, False)

  return upper_nodes_distance_k


def find_nodes_distance_k(tree, target, k):
  """ Handler function. """
  nodes_distance_k = []
  relationships = map_relationships(tree, tree.value, parent_value=None, rels={})

  target_entry = relationships[target]

  if k < 2: nodes_distance_k += target_entry["children"]
  else:
    for child in target_entry["children"]:
      nodes_distance_k += get_lower_nodes_distance_k(child, relationships, k - 1)
  
  if target_entry["parent"]:
    nodes_distance_k += get_upper_nodes_distance_k(target, [target], relationships, k, True)

  return list(set(nodes_distance_k))


if __name__ == "__main__":
  temp = {}

  # nodes = [
  #   {"id": "1", "left": "2", "right": "3", "value": 1},
  #   {"id": "2", "left": "4", "right": "5", "value": 2},
  #   {"id": "3", "left": None, "right": "6", "value": 3},
  #   {"id": "4", "left": None, "right": None, "value": 4},
  #   {"id": "5", "left": None, "right": None, "value": 5},
  #   {"id": "6", "left": "7", "right": "8", "value": 6},
  #   {"id": "7", "left": None, "right": None, "value": 7},
  #   {"id": "8", "left": None, "right": None, "value": 8}
  # ]
  nodes = [
    {"id": "1", "left": "2", "right": None, "value": 1},
    {"id": "2", "left": "3", "right": None, "value": 2},
    {"id": "3", "left": "4", "right": None, "value": 3},
    {"id": "4", "left": "5", "right": None, "value": 4},
    {"id": "5", "left": None, "right": None, "value": 5}
  ]
  # nodes = [
  #   {"id": "1", "left": "2", "right": "3", "value": 1},
  #   {"id": "2", "left": "4", "right": "5", "value": 2},
  #   {"id": "3", "left": "6", "right": "7", "value": 3},
  #   {"id": "4", "left": "8", "right": "9", "value": 4},
  #   {"id": "5", "left": None, "right": None, "value": 5},
  #   {"id": "6", "left": None, "right": None, "value": 6},
  #   {"id": "7", "left": None, "right": None, "value": 7},
  #   {"id": "8", "left": None, "right": None, "value": 8},
  #   {"id": "9", "left": None, "right": None, "value": 9}
  # ]
  # nodes = [
  #   {"id": "1", "left": "2", "right": "3", "value": 1},
  #   {"id": "2", "left": "4", "right": None, "value": 2},
  #   {"id": "3", "left": "5", "right": "6", "value": 3},
  #   {"id": "4", "left": None, "right": None, "value": 4},
  #   {"id": "5", "left": None, "right": None, "value": 5},
  #   {"id": "6", "left": None, "right": "7", "value": 6},
  #   {"id": "7", "left": None, "right": "8", "value": 7},
  #   {"id": "8", "left": None, "right": None, "value": 8}
  # ]
  # nodes = [
  #   {"id": "1", "left": "2", "right": "3", "value": 1},
  #   {"id": "2", "left": "4", "right": None, "value": 2},
  #   {"id": "3", "left": "5", "right": "6", "value": 3},
  #   {"id": "4", "left": None, "right": None, "value": 4},
  #   {"id": "5", "left": None, "right": None, "value": 5},
  #   {"id": "6", "left": None, "right": "7", "value": 6},
  #   {"id": "7", "left": None, "right": "8", "value": 7},
  #   {"id": "8", "left": None, "right": None, "value": 8}
  # ]
  # nodes = [
  #   {"id": "1", "left": "2", "right": "3", "value": 1},
  #   {"id": "2", "left": "4", "right": None, "value": 2},
  #   {"id": "3", "left": None, "right": "5", "value": 3},
  #   {"id": "4", "left": "6", "right": None, "value": 4},
  #   {"id": "5", "left": "7", "right": "8", "value": 5},
  #   {"id": "6", "left": None, "right": None, "value": 6},
  #   {"id": "7", "left": None, "right": None, "value": 7},
  #   {"id": "8", "left": None, "right": None, "value": 8}
  # ]

  for node in reversed(nodes):
    new_node = Node(node["value"])
    new_node.left = temp[node["left"]] if node["left"] in temp else node["left"]
    new_node.right = temp[node["right"]] if node["right"] in temp else node["right"]

    temp[node["id"]] = new_node

  root = temp[nodes[0]["id"]]

  # print(find_nodes_distance_k(root, 3, 2))
  print(find_nodes_distance_k(root, 2, 3))
  # print(find_nodes_distance_k(root, 8, 2))
  # print(find_nodes_distance_k(root, 8, 6))
  # print(find_nodes_distance_k(root, 3, 1))
  # print(find_nodes_distance_k(root, 6, 6))

