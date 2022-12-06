"""
Given 3 inputs, which are all instances of a node class that has name and direct ancestor k-v pairs, find the closest common ancestor to the two provided nodes to search.

TC: O(d) -- where d = height of the tree-shaped graph
SC: O(1) -- SC is constant regardless of number of nodes in the graph
"""
class Node:
  def __init__(self, name, ancestor):
    self.name = name
    self.ancestor = ancestor

def construct_graph(nodes, graph):
  for node in nodes:
    graph[node['name']] = Node(node['name'], graph[node['ancestor']] if node['ancestor'] else None)
  return graph

def node_depth(top, node):
  depth = 0
  while node != top:
    node = node.ancestor
    depth += 1
  return depth

"""
Function that improves on ancestor searching logic in solution.py.
"""
def backtrack_to_ancestor(lower, higher, depth_difference):
  while depth_difference > 0:
    lower, depth_difference = lower.ancestor, depth_difference - 1
  while lower != higher:
    lower, higher = lower.ancestor, higher.ancestor
  return lower

"""
Simplification of the core function from solution.py.
"""
def get_youngest_common_ancestor(top_ancestor, descendant_one, descendant_two):
  d1_depth, d2_depth = node_depth(top_ancestor, descendant_one), node_depth(top_ancestor, descendant_two)
  if d1_depth > d2_depth: return backtrack_to_ancestor(descendant_one, descendant_two, d1_depth - d2_depth)
  else: return backtrack_to_ancestor(descendant_two, descendant_one, d2_depth - d1_depth)

if __name__ == "__main__":
  # nodes = [
  #   {"ancestor": None, "id": "A", "name": "A"},
  #   {"ancestor": "A", "id": "B", "name": "B"},
  #   {"ancestor": "A", "id": "C", "name": "C"},
  #   {"ancestor": "B", "id": "D", "name": "D"},
  #   {"ancestor": "B", "id": "E", "name": "E"},
  #   {"ancestor": "C", "id": "F", "name": "F"},
  #   {"ancestor": "C", "id": "G", "name": "G"},
  #   {"ancestor": "D", "id": "H", "name": "H"},
  #   {"ancestor": "D", "id": "I", "name": "I"}
  # ]

  nodes = [
    {"ancestor": None, "id": "A", "name": "A"},
    {"ancestor": "A", "id": "B", "name": "B"},
    {"ancestor": "A", "id": "C", "name": "C"},
    {"ancestor": "A", "id": "D", "name": "D"},
    {"ancestor": "A", "id": "E", "name": "E"},
    {"ancestor": "A", "id": "F", "name": "F"},
    {"ancestor": "B", "id": "G", "name": "G"},
    {"ancestor": "B", "id": "H", "name": "H"},
    {"ancestor": "B", "id": "I", "name": "I"},
    {"ancestor": "C", "id": "J", "name": "J"},
    {"ancestor": "D", "id": "K", "name": "K"},
    {"ancestor": "D", "id": "L", "name": "L"},
    {"ancestor": "F", "id": "M", "name": "M"},
    {"ancestor": "F", "id": "N", "name": "N"},
    {"ancestor": "H", "id": "O", "name": "O"},
    {"ancestor": "H", "id": "P", "name": "P"},
    {"ancestor": "H", "id": "Q", "name": "Q"},
    {"ancestor": "H", "id": "R", "name": "R"},
    {"ancestor": "K", "id": "S", "name": "S"},
    {"ancestor": "P", "id": "T", "name": "T"},
    {"ancestor": "P", "id": "U", "name": "U"},
    {"ancestor": "R", "id": "V", "name": "V"},
    {"ancestor": "V", "id": "W", "name": "W"},
    {"ancestor": "V", "id": "X", "name": "X"},
    {"ancestor": "V", "id": "Y", "name": "Y"},
    {"ancestor": "X", "id": "Z", "name": "Z"}
  ]

  graph = construct_graph(nodes, {})
  print(get_youngest_common_ancestor(graph['A'], graph['T'], graph['H']))