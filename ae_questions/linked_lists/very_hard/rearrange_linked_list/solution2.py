"""

"""
class Node:
  """ Node class. Helps build LL data structure. """
  def __init__(self, value):
    self.value = value
    self.next = None

def traverse(head):
  """ Traverses a linked list to view node values in order. """
  order = []
  while head:
    order.append(head.value)
    head = head.next
  return order

def add_node(head, tail, node):
  if not head: head = tail = node
  else:
    tail.next = node
    tail = node
  return head, tail

def rearrange_linked_list(head, k):
  node = head
  smaller_head = smaller_tail = None
  equal_head = equal_tail = None
  greater_head = greater_tail = None

  while node:
    if node.value < k:
      smaller_head, smaller_tail = add_node(smaller_head, smaller_tail, node)
    elif node.value > k:
      greater_head, greater_tail = add_node(greater_head, greater_tail, node)
    else:
      equal_head, equal_tail = add_node(equal_head, equal_tail, node)

    prev = node
    prev.next, node = None, node.next

  h = greater_head
  if equal_head: h, equal_tail.next = equal_head, h
  if smaller_head: h, smaller_tail.next = smaller_head, h

  return h


if __name__ == "__main__":
  # nodes = [
  #   {"id": "5", "next": "0", "value": 5},
  #   {"id": "0", "next": "3", "value": 0},
  #   {"id": "3", "next": "2", "value": 3},
  #   {"id": "2", "next": "1", "value": 2},
  #   {"id": "1", "next": "4", "value": 1},
  #   {"id": "4", "next": None, "value": 4}
  # ]
  nodes = [
    {"id": "3", "next": "0", "value": 3},
    {"id": "0", "next": "5", "value": 0},
    {"id": "5", "next": "2", "value": 5},
    {"id": "2", "next": "1", "value": 2},
    {"id": "1", "next": "4", "value": 1},
    {"id": "4", "next": None, "value": 4}
  ]

  for i in reversed(range(len(nodes))):
    node = Node(nodes[i]["value"])
    if nodes[i]["next"]: node.next = nodes[i + 1]
    nodes[i] = node

  print(traverse(nodes[0]))

  l = rearrange_linked_list(nodes[0], 3)
  print(traverse(l))