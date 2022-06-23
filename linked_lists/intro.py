"""
Initial practice with the linked list data structure in Python.
Below is an implementation of a forward-looking, singly-linked list.
"""

# A node has two core properties: the data it holds, and the next Node to which it points.
# self.next is either None or a pointer to the next node's memory address.
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

# A LinkedList has one core property: head.
# head represents the first element in the linked list.
class LinkedList:
  def __init__(self):
    self.head = None

  def insert_at_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  def insert_at_end(self, data):
    new_node = Node(data)
    current = self.head
    while current.next is not None:
      current = current.next
    current.next = new_node

  def insert_at_position(self, data, position):
    new_node = Node(data)
    current = self.head
    p = 1
    while p < position - 1 and current.next is not None:
      current = current.next
      p += 1
    new_node.next = current.next
    current.next = new_node

  def traverse(self):
    current = self.head
    while current is not None:
      print(current.data)
      current = current.next

def main():
  linked_list = LinkedList()
  linked_list.insert_at_beginning(3)
  linked_list.insert_at_beginning(2)
  linked_list.insert_at_beginning(1)
  linked_list.insert_at_end(5)
  linked_list.insert_at_position(6, 6)
  linked_list.insert_at_position(4, 4)

  linked_list.traverse()

if __name__ == "__main__":
  main()