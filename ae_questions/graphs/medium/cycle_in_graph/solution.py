"""
Given an adjacency list for a graph (directed, unweighted), write a function that returns a boolean indicating whether or not the graph contains a cycle.

TC: max O((v + e) * v) -- "if edge in ways" means there's an O(n) search method called within an O(v + e) TC double for-loop
SC: O(v)
"""
def cycle_in_graph(edges):
  ways = {}
  for edge in range(len(edges)):
    for v in edges[edge]:
      if v == edge: return True
      if edge in ways:
        if v in ways[edge]: return True
        ways[v] = ways[edge] + [edge]
      else: ways[v] = [edge]

  return False

if __name__ == "__main__":
  # print(cycle_in_graph([
  #   [1, 3],
  #   [2, 3, 4],
  #   [0],
  #   [],
  #   [2, 5],
  #   []
  # ]))

  print(cycle_in_graph([
    [1],
    [2, 3, 4, 5, 6, 7],
    [],
    [2, 7],
    [5],
    [],
    [4],
    []
  ]))

  # print(cycle_in_graph([
  #   [1, 2],
  #   [2],
  #   []
  # ]))

  # print(cycle_in_graph([
  #   [1, 2],
  #   [2],
  #   [1]
  # ]))

  # print(cycle_in_graph([
  #   [0],
  #   [1]
  # ]))