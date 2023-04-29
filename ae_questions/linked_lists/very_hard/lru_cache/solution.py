"""


"""
class Node:
  def __init__(self, k, v):
    self.key = k
    self.value = v
    self.next = None

class LRUCache:
  def __init__(self, maxSize):
    self.maxSize = maxSize or 1
    self.root = None

  def traverse(self):
    curr = self.root
    while curr:
      print(curr.key, curr.value)
      curr = curr.next

  def trim_cache(self):
    curr, count = self.root, 0
    while curr.next:
      count += 1
      if count == 3: curr.next = None
      else: curr = curr.next

  def insertKeyValuePair(self, key, value):
    if not self.root:
      self.root = Node(key, value)
    else:
      nxt, self.root = self.root, Node(key, value)
      self.root.next = nxt
      self.trim_cache()

  def getValueFromKey(self, key):
    # Write your code here.
    pass

  def getMostRecentKey(self):
    # Write your code here.
    pass


if __name__ == "__main__":
  c = LRUCache(3)
  c.insertKeyValuePair("d", 4)
  c.insertKeyValuePair("c", 3)
  c.insertKeyValuePair("b", 2)
  c.insertKeyValuePair("a", 1)
  c.insertKeyValuePair("g", 7)
  c.traverse()