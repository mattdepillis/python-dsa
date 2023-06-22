"""

"""
class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

def find_nodes_distance_k(tree, target, k):
  return tree


if __name__ == "__main__":
  temp = {}

  nodes = [
    {"id": "1", "left": "2", "right": "3", "value": 1},
    {"id": "2", "left": "4", "right": "5", "value": 2},
    {"id": "3", "left": None, "right": "6", "value": 3},
    {"id": "4", "left": None, "right": None, "value": 4},
    {"id": "5", "left": None, "right": None, "value": 5},
    {"id": "6", "left": "7", "right": "8", "value": 6},
    {"id": "7", "left": None, "right": None, "value": 7},
    {"id": "8", "left": None, "right": None, "value": 8}
  ]

  for node in reversed(nodes):
    new_node = Node(node["value"])
    new_node.left = temp[node["left"]] if node["left"] in temp else node["left"]
    new_node.right = temp[node["right"]] if node["right"] in temp else node["right"]

    temp[node["id"]] = new_node

  root = temp[nodes[0]["id"]]

  print(find_nodes_distance_k(root, 3, 2))

