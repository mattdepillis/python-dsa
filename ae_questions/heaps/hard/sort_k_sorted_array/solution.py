"""
Given an array of size n and a value k, write an algorithm that sorts the input array in k-relative time. k signifies the max number of positions an item may be currently located in the array from its end sorted position.

TC: O(n * log(k)) -- iterate through n times but find min value from heap of size k
SC: O(k) -- temp heap at each index n
"""
def swap(heap, child, parent):
  heap[child], heap[parent] = heap[parent], heap[child]

def sift_up(heap, i):
  """ Sifts a node in the heap up by continually swapping with its parent if value is less than parent's. """
  while i > 0:
    parent = (i - 1) // 2
    if heap[i] < heap[parent]:
      swap(heap, i, parent)
      i = parent
    else: break

def sort_heap(arr, i, k):
  """ Creates a temporary heap of size k + 1 and sorts the min value to the top. """
  end = i + k + 1
  while end > len(arr): end -= 1

  heap = arr[i: end]
  for idx in reversed(range(len(heap))):
    sift_up(heap, idx)

  arr[i: end] = heap
  return arr

def sort_k_sorted_array(array, k):
  """ Handler function. """
  for i in range(len(array)):
    array = sort_heap(array, i, k)
  return array


if __name__ == "__main__":
  print(sort_k_sorted_array(
    [3, 2, 1, 5, 4, 7, 6, 5], 3
  ))

  print(sort_k_sorted_array(
    [4, 3, 2, 1, 2, 5, 6], 4
  ))