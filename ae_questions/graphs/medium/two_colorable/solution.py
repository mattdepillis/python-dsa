"""
Given an adjacency list of edges of a graph, write a function that returns whether or not the graph is two-colorable (each node assigned a "color", and no two connected nodes share the same color assignment).

TC: O(v + e) -- loop through all vertices and their edges
SC: O(v) -- store all vertices
"""
def two_colorable(edges):
  vertices, colors = {}, ["bl", "gr"]

  for edge in range(len(edges)):
    if not edge in vertices: vertices[edge] = colors[0]

    neighbor_color_index = colors.index(vertices[edge]) - 1

    for neighbor in edges[edge]:
      if not neighbor in vertices: vertices[neighbor] = colors[neighbor_color_index]
      elif not vertices[neighbor] == colors[neighbor_color_index]: return False

  return True


if __name__ == "__main__":
  # print(two_colorable([
  #   [1, 2],
  #   [0, 2],
  #   [0, 1]
  # ]))

  print(two_colorable([
    [1, 4],
    [0, 2, 3],
    [1, 4],
    [1],
    [0, 2]
  ]))