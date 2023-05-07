"""
Given a linked list, return the middle node. If there are 2 candidates for the middle node, return the second.

TC: O(n) - go through all nodes at least once.
SC: O(1) - constant memory, no matter the list size
"""
class LinkedList:
  def __init__(self, value):
    self.value = value
    self.next = None

def find_list_length(root):
  count = 0
  while root:
    count += 1
    root = root.next
  return count

def get_middle_node(root, middle_index):
  idx = 0
  while idx < middle_index:
    root = root.next
    idx += 1
  return root

def middle_node(root):
  list_length = find_list_length(root)
  middle_index = list_length // 2

  return get_middle_node(root, middle_index)


def generate_list(nodes):
  list_container = []
  for i in reversed(range(len(nodes))):
    node = LinkedList(nodes[i]['value'])
    if nodes[i]['next']: node.next = list_container[0]
    list_container.insert(0, node)
  return list_container[0]


if __name__ == "__main__":
  nodes = [
    {"id": "1", "next": "1-2", "value": 1},
    {"id": "1-2", "next": "1-3", "value": 1},
    {"id": "1-3", "next": "1-4", "value": 1},
    {"id": "1-4", "next": "2", "value": 1},
    {"id": "2", "next": "3", "value": 2},
    {"id": "3", "next": "4", "value": 3},
    {"id": "4", "next": "5", "value": 4},
    {"id": "5", "next": "5-2", "value": 5},
    {"id": "5-2", "next": "7", "value": 5},
    {"id": "7", "next": "10", "value": 7},
    {"id": "10", "next": None, "value": 10}
  ]
  
  root = generate_list(nodes)
  
  middle = middle_node(root)
  print('m', middle.value)
