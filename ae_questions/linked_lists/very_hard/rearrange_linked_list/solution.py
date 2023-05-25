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

def swap(prev, curr, next):
  new_next = next.next
  prev.next = next
  next.next = curr
  curr.next = new_next

  # previous next will now be previous to current node
  return next

def sort_in_order(curr, prev):
  while True:
    if curr.value > curr.next.value:
      prev = swap(prev, curr, curr.next)
    else: break

def rearrange_linked_list(head, k):
  start = curr = head
  last_unordered = last_ordered = head

  while curr.next:
    nxt = curr.next

    if curr.value >= k:
      if curr.value > curr.next.value:
        new_next = nxt.next
        if last_unordered.value >= k:
          nxt.next = curr
          start = last_unordered = nxt
        else:
          first_ordered = last_unordered.next
          last_unordered.next = nxt
          nxt.next = first_ordered
          if nxt.value < k:
            last_unordered = nxt
          else:
            sort_in_order(nxt, last_unordered)
          
        curr.next = new_next
      else:
        last_ordered = curr.next
        curr = curr.next

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
