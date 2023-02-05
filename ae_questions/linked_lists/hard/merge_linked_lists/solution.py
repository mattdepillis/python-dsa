"""
"""
class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

# list traversal helper function
def traverse_list(head):
  list = []
  while head:
    list.append(head.value)
    head = head.next
  return list


def merge_linked_lists(one, two):
  curr_one, curr_two = one, two
  head = one if one.value <= two.value else two

  if head == one: curr_one = curr_one.next
  else: curr_two = curr_two.next

  prev, nxt = head, None

  while curr_one and curr_two:
    if curr_one and curr_one.value <= curr_two.value:
      nxt, curr_one = curr_one, curr_one.next
    else:
      nxt, curr_two = curr_two, curr_two.next

    prev.next = prev = nxt

  if curr_one: prev.next = curr_one
  if curr_two: prev.next = curr_two

  return head


if __name__ == "__main__":
  head_one = None
  # nodes_one = [
  #   {"id": "2", "next": "6", "value": 2},
  #   {"id": "6", "next": "7", "value": 6},
  #   {"id": "7", "next": "8", "value": 7},
  #   {"id": "8", "next": None, "value": 8}
  # ]
  nodes_one = [
    {"id": "6", "next": "7", "value": 6},
    {"id": "7", "next": "8", "value": 7},
    {"id": "8", "next": "9", "value": 8},
    {"id": "9", "next": "10", "value": 9},
    {"id": "10", "next": None, "value": 10}
  ]
  # create first linked list
  for node in reversed(nodes_one):
    n = Node(node["value"])
    if head_one: n.next = head_one
    head_one = n

  head_two = None
  # nodes_two = [
  #   {"id": "1", "next": "3", "value": 1},
  #   {"id": "3", "next": "4", "value": 3},
  #   {"id": "4", "next": "5", "value": 4},
  #   {"id": "5", "next": "9", "value": 5},
  #   {"id": "9", "next": "10", "value": 9},
  #   {"id": "10", "next": None, "value": 10}
  # ]
  nodes_two = [
    {"id": "1", "next": "2", "value": 1},
    {"id": "2", "next": "3", "value": 2},
    {"id": "3", "next": "4", "value": 3},
    {"id": "4", "next": "5", "value": 4},
    {"id": "5", "next": None, "value": 5}
  ]
  # create second linked list
  for node in reversed(nodes_two):
    n = Node(node["value"])
    if head_one: n.next = head_two
    head_two = n

  merged = merge_linked_lists(head_one, head_two)
  print(traverse_list(merged))