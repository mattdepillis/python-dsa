"""
Implement a class for a LRU (least-recently used) cache.
The class should support the following methods, each with constant runtime:
- inserting k,v pairs
- retrieving value from key
- retrieve most recently used key

Notes:
- the size of the cache shouldn't exceed ```self.maxSize```
- if it does, the least-recently used item in the cache should be evicted
- if a key is inserted but it already exists in the cache, the new value should overwrite the old
- a cache node jumps to the root of the LL when added or its key is read.

TC (all methods): O(1) -- given the maxSize of the cache stays constant, all operations will be of roughly the same time complexity.
SC: O(1) -- max-size of the cache is constant.
"""

class Node:
  """ Class to represent LinkedList nodes """
  def __init__(self, k, v):
    self.key = k
    self.value = v
    self.next = None

class LRUCache:
  def __init__(self, maxSize):
    self.maxSize = maxSize or 1
    self.root = None

  def traverse(self):
    """ Traverses the LL and prints all k,v pairs. Used for visibility into LL order at a given time. """
    curr = self.root
    while curr:
      print(curr.key, curr.value)
      curr = curr.next

  def trim_cache(self):
    """ Trims the cache if needed to ensure it complies with max cache size. """
    curr, count = self.root, 0
    while curr.next:
      count += 1
      if count == self.maxSize: curr.next = None
      else: curr = curr.next

  def check_existing(self, key):
    """ Checks whether a node with the given key already exists in the cache. """
    curr = self.root
    while curr:
      if curr.key == key: return curr
      curr = curr.next
    return None

  def insertKeyValuePair(self, key, value):
    """
    Inserts a node into the cache.
    Will overwrite node value if a node with the provided key exists.
    Else, will insert a node as root. If necessary, will trim the cache to the max size after insertion.
    """
    if not self.root:
      self.root = Node(key, value)
    else:
      prev = self.check_existing(key)
      if prev:
        prev.value = value
        self.reorder_cache(prev.key)
      else:
        nxt, self.root = self.root, Node(key, value)
        self.root.next = nxt
        self.trim_cache()

  def reorder_cache(self, key):
    """
    Reorders the cache items.
    Used in tandem with getValueFromKey, as that node must move to root.
    """
    curr = self.root
    while curr.next:
      if curr.next.key == key:
        new_root = curr.next
        new_root.next, curr.next = self.root, new_root.next
        self.root = new_root
        return
      curr = curr.next

  def getValueFromKey(self, key):
    """ Gets the value at a given node with the specified key, if found. """
    curr = self.root
    while curr:
      if curr.key == key:
        v = curr.value
        self.reorder_cache(key)
        return v
      curr = curr.next
    return None

  def getMostRecentKey(self):
    """ Retrieves the root node's key. """
    return self.root.key


if __name__ == "__main__":
  """ Test Case 1 """
  # c = LRUCache(3)
  # c.insertKeyValuePair("d", 4)
  # c.insertKeyValuePair("c", 3)
  # c.insertKeyValuePair("b", 2)
  # print(c.getValueFromKey("d"))
  # c.insertKeyValuePair("c", 3)
  # c.traverse() # this should return c -> b -> d

  """ Test Case 2 """
  c = LRUCache(1)
  c.insertKeyValuePair("a", 1)
  print(c.getValueFromKey("a"))
  c.insertKeyValuePair("a", 3)
  print(c.getValueFromKey("a"))
  # c.traverse()
  c.insertKeyValuePair("b", 5)
  c.traverse()


  # {
  #   "arguments": ["b", 2],
  #   "method": "insertKeyValuePair",
  #   "output": null
  # },
  # {
  #   "arguments": ["a", 1],
  #   "method": "insertKeyValuePair",
  #   "output": null
  # },
  # {
  #   "arguments": ["c", 3],
  #   "method": "insertKeyValuePair",
  #   "output": null
  # },
  # {
  #   "arguments": [],
  #   "method": "getMostRecentKey",
  #   "output": "c"
  # },
  # {
  #   "arguments": ["a"],
  #   "method": "getValueFromKey",
  #   "output": 1
  # },
  # {
  #   "arguments": [],
  #   "method": "getMostRecentKey",
  #   "output": "c"
  # },
  # {
  #   "arguments": ["d", 4],
  #   "method": "insertKeyValuePair",
  #   "output": null
  # },
  # {
  #   "arguments": ["b"],
  #   "method": "getValueFromKey",
  #   "output": null
  # },
  # {
  #   "arguments": ["a", 5],
  #   "method": "insertKeyValuePair",
  #   "output": null
  # },
  # {
  #   "arguments": ["a"],
  #   "method": "getValueFromKey",
  #   "output": 5
  # }