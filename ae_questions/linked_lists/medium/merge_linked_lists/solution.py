"""
Given 2 linked lists of lengths m and n, which may potentially merge at an intersection node, write a function that returns the intersection node if it exists, or None if it doesn't.

TC:
SC:
"""
class ListNode:
  def __init__(self, value):
    self.value = value
    self.next = None

# small helper function to calculate list length
def calculate_list_length(list):
  length = 0
  while list: length, list = length + 1, list.next
  return length

def merge_linked_lists(list1, list2):
  list1_length, list2_length = calculate_list_length(list1), calculate_list_length(list2)

  longer, shorter = (list1, list2) if list1_length >= list2_length else (list2, list1)
  len_longer, len_shorter = max(list1_length, list2_length), min(list1_length, list2_length)

  while len_longer > len_shorter:
    longer, len_longer = longer.next, len_longer - 1

  while longer:
    if longer == shorter: return longer
    longer, shorter = longer.next, shorter.next

  return None


if __name__ == "__main__":
  shared_node = ListNode(4)

  list1_nodes, list1_container = [1, 2, 3], []
  list2_nodes, list2_container = [7, 6, 5], []

  for list in [list1_nodes, list2_nodes]:
    for i in reversed(range(len(list))):
      list[i] = ListNode(list[i])
      if i < len(list) - 1: list[i].next = list[i + 1]
    
  list1_nodes[len(list1_nodes) - 1].next = list2_nodes[len(list2_nodes) - 1].next = shared_node
  # list2_nodes[len(list2_nodes) - 1].next = shared_node

  print(merge_linked_lists(list1_nodes[0], list2_nodes[0]))