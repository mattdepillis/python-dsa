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

def rearrange_linked_list(head, k):
  start = curr = head
  prev = None
  unordered_end = ordered_start = ordered_end = None
  while curr.next:
    print('c', curr.value, curr.next.value)
    if curr.value >= k:
      two_next = curr.next.next
      one_next = curr.next

      one_next.next = curr
      curr.next = two_next

      print(f"one_next: {one_next.value if one_next else None}, curr: {curr.value if curr else None}, two_next: {two_next.value if two_next else None}")

      if prev: prev.next = one_next
      if curr == start: start = one_next
      
      prev = one_next
    else:
      prev = curr
      curr = curr.next

    if unordered_end: print(F"unordered_end: {unordered_end.value}")

  print(unordered_end.value)
  return start


if __name__ == "__main__":
  nodes = [
    {"id": "5", "next": "0", "value": 5},
    {"id": "0", "next": "3", "value": 0},
    {"id": "3", "next": "2", "value": 3},
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
