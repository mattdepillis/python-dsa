"""
"""
class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

def merge_linked_lists(one, two):
  return one, two

if __name__ == "__main__":
  head_one = None
  nodes_one = [
    {"id": "2", "next": "6", "value": 2},
    {"id": "6", "next": "7", "value": 6},
    {"id": "7", "next": "8", "value": 7},
    {"id": "8", "next": None, "value": 8}
  ]
  # create first linked list
  for node in reversed(nodes_one):
    n = Node(node["value"])
    if head_one: n.next = head_one
    head_one = n

  head_two = None
  nodes_two = [
    {"id": "1", "next": "3", "value": 1},
    {"id": "3", "next": "4", "value": 3},
    {"id": "4", "next": "5", "value": 4},
    {"id": "5", "next": "9", "value": 5},
    {"id": "9", "next": "10", "value": 9},
    {"id": "10", "next": None, "value": 10}
  ]
  # create second linked list
  for node in reversed(nodes_two):
    n = Node(node["value"])
    if head_one: n.next = head_two
    head_two = n

  print(merge_linked_lists(head_one, head_two))