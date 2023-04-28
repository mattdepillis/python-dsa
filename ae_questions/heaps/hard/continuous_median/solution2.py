"""
Write a ContinuousMedianHandler class. This class should:
- support continuous insertion of numbers
- should offer instant retrieval of the numbers' median
- should use the heap data structure to achieve this

TC (insert()): O(log(n))
  - only sift up the inserted number
  - if we need to remove a number from the longer heap, sifting both new values up and down is + 2 max O(log(n)) operations
SC: O(n) -- store n numbers
"""
class ContinuousMedianHandler:
  def __init__(self):
    self.median = None
    self.max_heap = []
    self.min_heap = []

  def determine_longer(self):
    """ Determines the longer and shorter of the two heaps. """
    if len(self.max_heap) > len(self.min_heap):
      longer, shorter = self.max_heap, self.min_heap
    else: longer, shorter = self.min_heap, self.max_heap
    return longer, shorter

  def balance_heap_lengths(self):
    """ Balances the length of the heaps when difference > 1. """
    (longer, shorter) = self.determine_longer()
    shorter.append(longer.pop(0))

    self.sift_up(shorter)
    self.sift_down(longer)
  
  def swap_with_parent(self, heap, child, parent):
    """
    Handles the swapping of a child value with a parent value on sift_up.
    if-else to handle different sift conditions for min and max heaps. 
    """
    if heap == self.max_heap and heap[child] > heap[parent]: return True
    elif heap == self.min_heap and heap[child] < heap[parent]: return True
    return False
 
  def sift_up(self, heap):
    """ Sifts a newly-added node up the heap, if needed. """
    i = len(heap) - 1
    while i > 0:
      parent_index = (i - 1) // 2
      if self.swap_with_parent(heap, i, parent_index):
        heap[i], heap[parent_index] = heap[parent_index], heap[i]
        i = parent_index
      else: break

  """ lambda to return bool: value less than another"""
  first_is_smaller = lambda self, x, y: x < y

  def find_min_child_index(self, heap, children):
    """ Finds the index of the parent node's minimum child"""
    if children[0] > len(heap) - 1: return None

    return children[0] if (
      children[1] > len(heap) - 1
      or self.first_is_smaller(heap[children[0]], heap[children[1]])
    ) else children[1]

  def sift_down(self, heap):
    """  Sifts the root down, if needed, whenever there is a change in the heap root value. """
    i = 0
    while i < len(heap) - 1:
      min_child_idx = self.find_min_child_index(heap, [(2 * i) + 1, (2 * i) + 2])
      if not min_child_idx: break
      
      if self.swap_with_parent(heap, min_child_idx, i):
        heap[i], heap[min_child_idx] = heap[min_child_idx], heap[i]
        i = min_child_idx
      else: break

  def insert(self, number):
    """ Handles insertion into a heap. """
    if not len(self.max_heap): self.max_heap.append(number)
    else:
      if number < self.max_heap[0]:
        self.max_heap.append(number)
        heap_to_sift = self.max_heap
      else:
        self.min_heap.append(number)
        heap_to_sift = self.min_heap
        
      self.sift_up(heap_to_sift)

      if abs(len(self.max_heap) - len(self.min_heap)) > 1:
        self.balance_heap_lengths()
      
      print(f"max_heap (smaller): {self.max_heap}, min_heap (larger): {self.min_heap}")
    self.set_median()

  def set_median(self):
    """ Sets the median of all inserted numbers differently depending on the total number of values. """
    if not (len(self.max_heap) == len(self.min_heap)):
      self.median = self.determine_longer()[0][0]
    else: self.median = (self.max_heap[0] + self.min_heap[0]) / 2

  def get_median(self):
    """ Simple retrieval method for class's median. """
    return self.median
    

if __name__ == "__main__":
  h = ContinuousMedianHandler()
  print(h.get_median())
  h.insert(10)
  print(h.get_median())
  h.insert(5)
  print(h.get_median())
  h.insert(15)
  print(h.get_median())
  h.insert(11)
  print(h.get_median())
  h.insert(34)
  print(h.get_median())
  h.insert(22)
  print(h.get_median())
  h.insert(25)
  print(h.get_median())
  h.insert(24)
  print(h.get_median())
  h.insert(17)
  print(h.get_median())
  h.insert(16)
  print(h.get_median())