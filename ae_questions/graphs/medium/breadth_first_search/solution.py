"""
Given a class ```Node``` that has a name and an array of optional children (when put together, nodes form a tree-like structure), implement the breadth-first search method on the class. The function should take in an empty array and return the array with all nodes, in the order in which they were visited.
"""
class Node:
  def __init__(self, name):
    self.name = name
    self.children = []

  def add_child(self, name):
    self.children.append(Node(name))
    return self

  def bfs_helper(self, array, queue):
    if self.name not in array:
      array.append(self.name)

      print(self.children)

      if len(self.children) > 0:
        print('true')
        queue.append(self)
    return (array, queue)

  def breadth_first_search(self, array):
    array.append(self.name)
    queue = []

    for child in self.children:
      child.bfs_helper(array, queue)

    print(queue)
    return array

    # if self.name not in array:
    #   array.append(self.name)
    
    # for child in self.children:
    #   child.breadth_first_search(array)

    # return array


if __name__ == "__main__":
  started, start_node = False, None

  a, b, c, d, e, f, g, h, i, j, k = Node('A'), Node('B'), Node('C'), Node('D'), Node('E'), Node('F'), Node('G'), Node('H'), Node('I'), Node('J'), Node('K')
  a.add_children()

  # nodes = [
  #   {"children": ["B", "C", "D"], "id": "A", "value": "A"},
  #   {"children": ["E", "F"], "id": "B", "value": "B"},
  #   {"children": [], "id": "C", "value": "C"},
  #   {"children": ["G", "H"], "id": "D", "value": "D"},
  #   {"children": [], "id": "E", "value": "E"},
  #   {"children": ["I", "J"], "id": "F", "value": "F"},
  #   {"children": ["K"], "id": "G", "value": "G"},
  #   {"children": [], "id": "H", "value": "H"},
  #   {"children": [], "id": "I", "value": "I"},
  #   {"children": [], "id": "J", "value": "J"},
  #   {"children": [], "id": "K", "value": "K"}
  # ]

  # TODO: use a dict to store each node. Then, append children to each node by circling through nodes array.
  # TODO: then, isolate start_node as A and perform BFS.

  # completed = []
  # for node in nodes:
  #   n = Node(node['value'])
  #   for child in node['children']:
  #     n.add_child(child)
  #   if not started:
  #     start_node = n
  #     started = True
    
  # print(start_node.breadth_first_search(array=[]))