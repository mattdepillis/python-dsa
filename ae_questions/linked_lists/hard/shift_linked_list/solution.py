"""

"""
class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

def traverse(curr, list):
  while curr:
    list.append(curr.value)
    curr = curr.next
  return list


def shift_linked_list(head, k):
  count, curr = 0, head

  while curr:
    count, curr = count + 1, curr.next

  r = count - (k % count)
  if r == count: return head

  curr = head
  while r > 1:
    r, curr = r - 1, curr.next

  new_head, curr.next = curr.next, None
  curr = new_head

  while curr.next: curr = curr.next
  curr.next, head = head, new_head

  return new_head


if __name__ == "__main__":
  nodes = [
    {"id": "0", "next": "1", "value": 0},
    {"id": "1", "next": "2", "value": 1},
    {"id": "2", "next": "3", "value": 2},
    {"id": "3", "next": "4", "value": 3},
    {"id": "4", "next": "5", "value": 4},
    {"id": "5", "next": None, "value": 5}
  ]
  head = None
  for i in reversed(range(len(nodes))):
    n = Node(nodes[i]["value"])
    if head: n.next = head
    head = n

  # print(traverse(head, list=[]))
  # l = shift_linked_list(head, 8)
  l = shift_linked_list(head, 0)
  # l = shift_linked_list(head, 6)
  print(traverse(l, list=[]))