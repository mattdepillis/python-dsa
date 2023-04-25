"""

"""
class MinHeap:
  def __init__(self, array):
    # Do not edit the line below.
    self.heap = self.buildHeap(array)

  def buildHeap(self, array):
    """
    Builds the heap, represented as a list, from an unsorted list.
    Finds the last current parent node and sifts all parents down.
    """
    last_parent = (len(array) - 2) // 2
    for i in reversed(range(0, last_parent + 1)):
      array = self.siftDown(i, array)
    return array

  def siftDown(self, i, array):
    """
    Recursively sifts a parent node down if it's greater than its smallest child.
    """
    if i > (len(array) - 2) // 2: return array

    if (2 * i) + 2 > len(array) - 1:
      min_child_index = (2 * i) + 1
    else:
      min_child_index = (2 * i) + 1 if (
        array[(2 * i) + 1] < array[(2 * i) + 2]
      ) else (2 * i) + 2

    if array[min_child_index] < array[i]:
      array[i], array[min_child_index] = array[min_child_index], array[i]
      array = self.siftDown(min_child_index, array)

    return array

  def siftUp(self):
    # Write your code here.
    pass

  def peek(self):
    # Write your code here.
    pass

  def remove(self):
    # Write your code here.
    pass

  def insert(self, value):
    # Write your code here.
    pass


if __name__ == "__main__":
  heap = MinHeap([48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41])
  print(heap.heap)