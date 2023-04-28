"""
Write a ContinuousMedianHandler class. This class should:
- support continuous insertion of numbers
- should offer instant retrieval of the numbers' median
- should use the heap data structure to achieve this

TC (insert()): O(nlog(n)) -- in this first iteration, sift_up for each index in the heap on insert (unoptimal)
SC: O(n) -- store n numbers
"""
class ContinuousMedianHandler:
  def __init__(self):
    self.median = None
    self.max_heap = []
    self.min_heap = []

  def determine_longer(self):
    if len(self.max_heap) > len(self.min_heap):
      longer, shorter = self.max_heap, self.min_heap
    else: longer, shorter = self.min_heap, self.max_heap
    return longer, shorter

  def balance_heap_lengths(self):
    (longer, shorter) = self.determine_longer()
    shorter.append(longer.pop(0))
    self.sift_heaps()
  
  def swap_with_parent(self, heap, child, parent):
    if heap == self.max_heap and heap[child] > heap[parent]: return True
    elif heap == self.min_heap and heap[child] < heap[parent]: return True
    return False
 
  def sift_up(self, heap):
    for i in range(1, len(heap)):
      while i > 0:
        parent_index = (i - 1) // 2
        if self.swap_with_parent(heap, i, parent_index):
          heap[i], heap[parent_index] = heap[parent_index], heap[i]
          i = parent_index
        else: break

  def sift_heaps(self):
    for heap in [self.min_heap, self.max_heap]:
      self.sift_up(heap)

  def insert(self, number):
    if not len(self.max_heap): self.max_heap.append(number)
    else:
      if number < self.max_heap[0]: self.max_heap.append(number)
      else: self.min_heap.append(number)
        
      self.sift_heaps()
      # print(f"BEFORE: max_heap (smaller): {self.max_heap}, min_heap (larger): {self.min_heap}")

      if abs(len(self.max_heap) - len(self.min_heap)) > 1:
        self.balance_heap_lengths()
      
      print(f"max_heap (smaller): {self.max_heap}, min_heap (larger): {self.min_heap}")
    self.set_median()

  def set_median(self):
    if not (len(self.max_heap) == len(self.min_heap)):
      self.median = self.determine_longer()[0][0]
    else: self.median = (self.max_heap[0] + self.min_heap[0]) / 2

  def get_median(self):
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