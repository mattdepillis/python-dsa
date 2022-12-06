"""
Given 3 inputs, which are all instances of a node class that has name and direct ancestor k-v pairs, find the closest common ancestor to the two provided nodes to search.
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
  depth, current = 1, node
  while current != top:
    current = current.ancestor
    depth += 1
  return depth

def get_youngest_common_ancestor(top_ancestor, descendant_one, descendant_two):
  if top_ancestor in (descendant_one, descendant_two):
    return top_ancestor

  d1_depth, d2_depth = node_depth(top_ancestor, descendant_one), node_depth(top_ancestor, descendant_two)

  deep, shallow = (descendant_one, descendant_two) if d1_depth > d2_depth else (descendant_two, descendant_one)

  if d1_depth != d2_depth:
    greater_depth, smaller_depth = (d1_depth, d2_depth) if d1_depth > d2_depth else (d2_depth, d1_depth)
    while greater_depth > smaller_depth:
      if deep.ancestor == shallow:
        return shallow.ancestor
      greater_depth -= 1
      deep = deep.ancestor

  a1, a2 = deep, shallow
  while True:
    if a1.ancestor == a2.ancestor:
      return a1.ancestor
    a1, a2 = a1.ancestor, a2.ancestor

if __name__ == "__main__":
  nodes = [
    {"ancestor": None, "id": "A", "name": "A"},
    {"ancestor": "A", "id": "B", "name": "B"},
    {"ancestor": "A", "id": "C", "name": "C"},
    {"ancestor": "B", "id": "D", "name": "D"},
    {"ancestor": "B", "id": "E", "name": "E"},
    {"ancestor": "C", "id": "F", "name": "F"},
    {"ancestor": "C", "id": "G", "name": "G"},
    {"ancestor": "D", "id": "H", "name": "H"},
    {"ancestor": "D", "id": "I", "name": "I"}
  ]
  graph = construct_graph(nodes, {})

  print(get_youngest_common_ancestor(graph['A'], graph['E'], graph['I']))
