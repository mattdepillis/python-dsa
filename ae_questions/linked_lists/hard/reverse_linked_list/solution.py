"""
Write a function that takes a head of a singly-linked list and reverses it in-place.

TC: O(n) -- but suboptimal, as this is a 2n (double-pass) solution
SC: O(n) -- this is actually an O(n) solution, as a new key must be stored at each node
"""
class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

def reverse_linked_list(node):
  current, prev = node, None
  while current:
    current.prev = prev
    prev, current = current, current.next
  
  current = prev
  while current:
    current.next = current.prev
    del current.prev
    current = current.next
  return prev


if __name__ == "__main__":
  nodes = [
    {"id": "0", "next": "1", "value": 0},
    {"id": "1", "next": "2", "value": 1},
    {"id": "2", "next": "3", "value": 2},
    {"id": "3", "next": "4", "value": 3},
    {"id": "4", "next": "5", "value": 4},
    {"id": "5", "next": None, "value": 5}
  ]
  node_list = [None for _ in nodes]

  for n in reversed(range(len(nodes))):
    val, nxt = nodes[n]["value"], nodes[n]["next"]
    node = Node(val)
    if nxt: node.next = node_list[int(nxt)]
    node_list[n] = node

  print(reverse_linked_list(node_list[0]))
