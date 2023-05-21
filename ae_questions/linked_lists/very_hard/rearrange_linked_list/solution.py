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
  start = head
  curr = head.next
  last_unordered = last_ordered = head
  while curr.next:
    nxt = curr.next
    print(f"curr: {curr.value if curr else None}, lo: {last_ordered.value if last_ordered else None}, lu: {last_unordered.value if last_unordered else None}")
    if curr.value < k:
      if last_ordered == last_unordered:
        start = last_unordered = curr
        curr.next = last_ordered
      else:
        first_ordered = last_unordered.next
        curr.next = first_ordered
        last_unordered.next = curr
        last_unordered = curr

      last_ordered.next = nxt
      curr = last_ordered.next
    else:
      last_ordered = curr
    
      curr = nxt

      

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
