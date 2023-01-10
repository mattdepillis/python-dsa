"""
Given an adjacency list for a graph (directed, unweighted), write a function that returns a boolean indicating whether or not the graph contains a cycle.

NOTE: this solution improves upon solution 1 (which might contain O(n) operations for given stack searching operations) by using a stack DS and DFS to determine whether a node a) has already been visited and if not, to continue DFSing to see if a node is visited twice in the process of recursion, or b) is already in the stack (at which point True is returned)

TC: O(v + e) -- skip nodes that have already been visited; use of a stack
SC: O(v)
"""
def recurse(node, edges, visited, stack):
  visited[node] = True
  stack[node] = True

  for neighbor in edges[node]:
    if not visited[neighbor]:
      visited[neighbor] = True
      if recurse(neighbor, edges, visited, stack): return True
    elif stack[neighbor]: return True

  stack[node] = False
  return False

def cycle_in_graph(edges):
  visited = stack = [False for _ in edges]

  for i in range(len(edges)):
    if visited[i]: continue
    if recurse(i, edges, visited, stack): return True

  return False

if __name__ == "__main__":
  print(cycle_in_graph([
    [1, 3],
    [2, 3, 4],
    [0],
    [],
    [2, 5],
    []
  ]))

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