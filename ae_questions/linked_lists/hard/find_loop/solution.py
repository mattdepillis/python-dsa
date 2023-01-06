"""
Write a function that takes the head of a singly-linked list and...
"""
class Node:
  def __init__(self, value, nxt):
    self.value = value
    self.next = nxt

def find_loop(node):
  while node:
    if isinstance(node.value, str):
      node.value = int(node.value)
      break
    node.value = str(node.value)
    node = node.next

  origin, current = node, node.next

  while current is not origin:
    current.value = int(current.value)
    current = current.next
  return origin


if __name__ == "__main__":
  # holding data structure for nodes
  dict = {}

  nodes = [
    {"id": "0", "next": "1", "value": 0},
    {"id": "1", "next": "2", "value": 1},
    {"id": "2", "next": "3", "value": 2},
    {"id": "3", "next": "4", "value": 3},
    {"id": "4", "next": "5", "value": 4},
    {"id": "5", "next": "6", "value": 5},
    {"id": "6", "next": "7", "value": 6},
    {"id": "7", "next": "8", "value": 7},
    {"id": "8", "next": "9", "value": 8},
    {"id": "9", "next": "4", "value": 9}
  ]

  for node in nodes:
    node_value, next_node = node["value"], int(node["next"])
    dict[node_value] = Node(node_value, next_node)

  for value in dict:
    next_node = dict[value].next
    dict[value].next = dict[next_node]

  head = dict[0]

  print(find_loop(head))

