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

  def check_existing(self, key):
    curr = self.root
    while curr:
      if curr.key == key: return curr
      curr = curr.next
    return None

  def insertKeyValuePair(self, key, value):
    if not self.root:
      self.root = Node(key, value)
    else:
      nxt, self.root = self.root, Node(key, value)
      self.root.next = nxt
      self.trim_cache()

  def reorder_cache(self, key):
    curr = self.root
    while curr.next:
      if curr.next.key == key:
        new_root = curr.next
        new_root.next, curr.next = self.root, new_root.next
        self.root = new_root
        return
      curr = curr.next

  def getValueFromKey(self, key):
    curr = self.root
    while curr:
      if curr.key == key: return curr.value
      curr = curr.next
    return None

  def getMostRecentKey(self):
    return self.root.key


if __name__ == "__main__":
  c = LRUCache(3)
  c.insertKeyValuePair("d", 4)
  c.insertKeyValuePair("c", 3)
  c.insertKeyValuePair("b", 2)
  c.insertKeyValuePair("a", 1)
  c.insertKeyValuePair("g", 7)
  c.traverse()
  x = c.getValueFromKey("f")
  print(x)
  print(c.getMostRecentKey())


  {
    "arguments": ["b", 2],
    "method": "insertKeyValuePair",
    "output": null
  },
  {
    "arguments": ["a", 1],
    "method": "insertKeyValuePair",
    "output": null
  },
  {
    "arguments": ["c", 3],
    "method": "insertKeyValuePair",
    "output": null
  },
  {
    "arguments": [],
    "method": "getMostRecentKey",
    "output": "c"
  },
  {
    "arguments": ["a"],
    "method": "getValueFromKey",
    "output": 1
  },
  {
    "arguments": [],
    "method": "getMostRecentKey",
    "output": "c"
  },
  {
    "arguments": ["d", 4],
    "method": "insertKeyValuePair",
    "output": null
  },
  {
    "arguments": ["b"],
    "method": "getValueFromKey",
    "output": null
  },
  {
    "arguments": ["a", 5],
    "method": "insertKeyValuePair",
    "output": null
  },
  {
    "arguments": ["a"],
    "method": "getValueFromKey",
    "output": 5
  }