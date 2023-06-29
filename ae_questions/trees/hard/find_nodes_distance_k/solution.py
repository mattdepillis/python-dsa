"""

"""
class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

def map_relationships(node, parent, rels):
  entry = {
    "parent": parent, "children": []
  }

  if node.left: entry["children"].append(node.left)
  if node.right: entry["children"].append(node.right)

  for child in entry["children"]: map_relationships(child, node, rels)
  rels[node.value] = entry

  return rels


def get_lower_nodes_distance_k(value, relationships, k_remaining):
  entry = relationships[value]

  if k_remaining == 1: return entry["children"]
  lower_nodes_distance_k = []

  for child in entry["children"]:
    lower_nodes_distance_k += get_lower_nodes_distance_k(child.value, relationships, k_remaining - 1)

  return lower_nodes_distance_k

def get_upper_nodes_distance_k(value, visited, relationships, k, up):
  print('k_rem', k, 'value', value)

  if k == 1:
    nk = [child for child in relationships[value]['children'] if child.value not in visited]
    print('nk', nk)
    if relationships[value]['parent'] and up and relationships[value]['parent'].value not in visited: nk += [relationships[value]['parent']]
    print('nk now', nk)
    return nk

  upper_nodes_distance_k = []

  if relationships[value]['parent']:
    visited += [relationships[value]['parent'].value]
    upper_nodes_distance_k += get_upper_nodes_distance_k(relationships[value]['parent'].value, visited, relationships, k - 1, True)
  if k > 1:
    for child in relationships[value]['children']:
      if not child.value in visited:
        visited += [child.value]
        upper_nodes_distance_k += get_upper_nodes_distance_k(child.value, visited, relationships, k - 1, False)

  return upper_nodes_distance_k


def find_nodes_distance_k(tree, target, k):
  nodes_distance_k = []
  relationships = map_relationships(tree, parent=None, rels={})
  # print(relationships)

  target_entry = relationships[target]

  if k < 2: nodes_distance_k += target_entry["children"]
  else:
    for child in target_entry["children"]:
      nodes_distance_k += get_lower_nodes_distance_k(child.value, relationships, k - 1)

  print('lower', [node.value for node in nodes_distance_k])
  
  if target_entry["parent"]:
    nodes_distance_k += get_upper_nodes_distance_k(target, [target], relationships, k, True)

  included, nk = set(), []
  for node in nodes_distance_k:
    if node.value in included: continue
    else:
      nk.append(node.value)
      included.add(node.value)

  return nk


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

