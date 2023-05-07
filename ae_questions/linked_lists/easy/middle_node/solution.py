"""


"""
class LinkedList:
  def __init__(self, value):
    self.value = value
    self.next = None

def middle_node(linked_list):
  return linked_list


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
  print('m', middle)
