"""
Given a class ```Node``` that has a name and an array of optional children (when put together, nodes form a tree-like structure), implement the breadth-first search method on the class. The function should take in an empty array and return the array with all nodes, in the order in which they were visited.

Solution: add the root node to the queue. Then, while the queue length is greater than 0, pass the array and queue into the helper function and return the new queue (full of the previous queue's children) to the queue var in the while loop.

TC: O(v + e), where v = vertices and e = edges in the graph.
  - NOTE: for a tree, this will be O(v)
SC: O(v)
"""
class Node:
  def __init__(self, name):
    self.name = name
    self.children = []

  def add_child(self, node):
    self.children.append(node)
    return self

  def bfs_helper(self, array, queue):
    q = []

    for item in queue:
      array.append(item.name)
      for child in item.children:
        q.append(child)

    queue = []
    for child in q:
      queue.append(child)

    return queue
  
  def breadth_first_search(self, array):
    queue = []
    queue.append(self)

    while len(queue) > 0:
      queue = self.bfs_helper(array, queue)

    return array


if __name__ == "__main__":

  nodes = [
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
  ]

  # use a graph to create nodes and then add children iteratively
  temp = {}
  for node in nodes:
    temp[node['value']] = Node(node['value'])

  for node in nodes:
    n = temp[node['value']]
    for child in node['children']:
      n.add_child(temp[child])

  for child in temp['A'].children:
    print('c', child.name)
    
  print(temp['A'].breadth_first_search(array=[]))