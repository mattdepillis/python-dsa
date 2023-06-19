"""

"""
def swap(heap, child, parent):
  heap[child], heap[parent] = heap[parent], heap[child]

def sift_up(heap, i):
  while i > 0:
    parent = (i - 1) // 2
    if heap[i] < heap[parent]:
      swap(heap, i, parent)
      i = parent
    else: break

def sort_heap(arr, i, k):
  end = i + k + 1
  while end > len(arr): end -= 1

  heap = arr[i: end]
  for idx in reversed(range(len(heap))):
    sift_up(heap, idx)
    
  arr[i: end] = heap
  return arr

def sort_k_sorted_array(array, k):
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