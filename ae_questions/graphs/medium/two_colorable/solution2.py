"""
Given an adjacency list of edges of a graph, write a function that returns whether or not the graph is two-colorable (each node assigned a "color", and no two connected nodes share the same color assignment).

TC: O(v + e) -- loop through all vertices and their edges
SC: O(v) -- store all vertices
"""
def two_colorable(edges):
  colors = [None for _ in edges]
  colors[0], stack = True, [0]

  while len(stack) > 0:
    v = stack.pop()
    for e in edges[v]:
      if colors[e] is None:
        colors[e] = not colors[v] 
        stack.append(e)
      elif colors[e] == colors[v]: return False
  
  return True


if __name__ == "__main__":
  print(two_colorable([
    [1, 4],
    [0, 2, 3],
    [1, 4],
    [1],
    [0, 2]
  ]))