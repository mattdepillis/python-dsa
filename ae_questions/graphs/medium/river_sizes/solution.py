"""
River sizes algorithm.
"""
class Node:
  def __init__(self, value):
    self.value = value
    self.neighbors = []

def populate_graph(matrix):
  graph = {}
  for row in range(len(matrix)):
    graph[row] = []
    for i in range(len(matrix[row])):
      graph[row].append(Node(matrix[row][i]))
  return graph

def determine_neighbors(graph, row, index, width, height):
  neighbors, r = [], graph[row]
  if index == 0:
    neighbors += [None, r[index + 1]]
  elif index == width - 1:
    neighbors += [None, r[index - 1]]
  else:
    neighbors += [r[index - 1], r[index + 1]]

  if row == 0:
    neighbors += [None, graph[row + 1][index]]
  elif row == height - 1:
    neighbors += [None, graph[row - 1][index]]
  else:
    neighbors += [graph[row - 1][index], graph[row + 1][index]]
  return neighbors

def dfs_rivers(node, visited, count):
  if node not in visited:
    visited.append(node)
    if node.value == 1:
      count += 1
      for n in node.neighbors:
        if n:
          count = dfs_rivers(n, visited, count)
  return count

def river_sizes(matrix):
  graph, width, height = populate_graph(matrix), len(matrix[0]), len(matrix)

  for row in graph:
    for i, node in enumerate(graph[row]):
      node.neighbors = determine_neighbors(graph, row, i, width, height)

  visited, rivers = [], []
  for row in graph:
    for node in graph[row]:
      if node.value == 1 and node not in visited:
        rivers += [dfs_rivers(node, visited, 0)]

  return rivers


if __name__ == "__main__":
  print(river_sizes([
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0]
  ]))