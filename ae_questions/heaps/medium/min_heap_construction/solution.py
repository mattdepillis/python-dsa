"""

"""
import math

class MinHeap:
  def __init__(self, array):
    # Do not edit the line below.
    self.heap = self.buildHeap(array)

  def buildHeap(self, array):
    """
    Builds the heap, represented as a list, from an unsorted list.
    Finds the last current parent node and sifts all parents down.
    """
    self.heap = array
    last_parent = (len(array) - 2) // 2
    for i in reversed(range(0, last_parent + 1)):
      self.siftDown(i)
    return self.heap

  def siftDown(self, i):
    """
    Recursively sifts a parent node down if it's greater than its smallest child.
    """
    if i > (len(self.heap) - 2) // 2: return

    if (2 * i) + 2 > len(self.heap) - 1:
      min_child_index = (2 * i) + 1
    else:
      min_child_index = (2 * i) + 1 if (
        self.heap[(2 * i) + 1] < self.heap[(2 * i) + 2]
      ) else (2 * i) + 2

    if self.heap[min_child_index] < self.heap[i]:
      self.heap[i], self.heap[min_child_index] = self.heap[min_child_index], self.heap[i]
      self.siftDown(min_child_index)

  def siftUp(self, i):
    parent_index = math.floor((i - 1) // 2)
    if self.heap[i] < self.heap[parent_index]:
      self.heap[i], self.heap[parent_index] = self.heap[parent_index], self.heap[i]
      self.siftUp(parent_index)

  def peek(self):
    return self.heap[0]

  def remove(self):
    to_remove = self.heap[0]
    last = len(self.heap) - 1
    self.heap[0], self.heap[last] = self.heap[last], self.heap[0]
    self.heap.pop(last)
    self.siftDown(0)
    return to_remove

  def insert(self, value):
    self.heap.append(value)
    self.siftUp(len(self.heap) - 1)


if __name__ == "__main__":
  heap = MinHeap([48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41])
  print(heap.heap)
  heap.insert(76)
  print(heap.peek())
  heap.remove()
  print(heap.heap)
  print(heap.peek())
  heap.remove()
  print(heap.heap)
  print(heap.peek())
  heap.insert(87)
  print(heap.heap)