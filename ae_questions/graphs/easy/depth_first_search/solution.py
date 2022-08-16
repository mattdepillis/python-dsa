"""
Implement a graph class and write a depth-first search method that traverses the graph from left to right, starting with the startNode. The method should return an array of all nodes, in the order in which they were visited on traversal.
"""
class Graph:
  # do something
  def __init__(self, data):
    nodes, start = data['nodes'], data['start']

    self.graph = {}
    self.start = start

    for node in nodes:
      value, children = node['value'], node['children']
      self.graph[value] = children

    print(self.graph)

  def depth_first_search(self):
    visited = []
    def dfs(node):
      if node not in visited:
        visited.append(node)
        for child in self.graph[node]:
          dfs(child)
    dfs(self.start)
      
    return visited


if __name__ == "__main__":
  graph = Graph({
    "nodes": [
      {"children": ["B", "C", "D"], "id": "A", "value": "A"},
      {"children": ["E", "F"], "id": "B", "value": "B"},
      {"children": [], "id": "C", "value": "C"},
      {"children": ["G", "H"], "id": "D", "value": "D"},
      {"children": [], "id": "E", "value": "E"},
      {"children": ["I", "J"], "id": "F", "value": "F"},
      {"children": ["K"], "id": "G", "value": "G"},
      {"children": [], "id": "H", "value": "H"},
      {"children": [], "id": "I", "value": "I"},
      {"children": [], "id": "J", "value": "J"},
      {"children": [], "id": "K", "value": "K"}
    ],
    "start": "A"
  })
  print(graph.depth_first_search())
