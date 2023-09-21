"""
Write a function called heap_sort that accepts an array of integers as a parameter and returns the array sorted from smallest to largest via the Heap Sort algorithm.

TC: O(n * log(n)) -- iterates through n - 1 times; for each time, will perform approximately log(n) sets of parent-child value comparisons
SC: O(1) -- sorts the array in place
"""
def heap_sort(array):
  for i in range(len(array) - 1):
    top_of_heap = i

    """
    Slides the last parent along the array as i increases, to account for new top_of_heap index.
    For instance, with len(array) = 7, at i = 1 the numerator will equal 6 (the new heap size).
    The equation subtracts 1 to account for the end index of the array, and
    adds back i to scale the last parent to the proper index in the array.
    """
    last_parent_index = ((len(array) - i) // 2) - 1 + i

    for j in reversed(range(top_of_heap, last_parent_index + 1)):
      """
      Subtracts i from each child index to account for the current top of heap.
      For instance, at i = 4, with len(array) = 7, children of j = 4 are at idxs 5 and 6, not 9 and 10:
      [5, 6] = (8 + 1 - 4), (8 + 2 - 4).
      """
      children = [(2 * j + 1 - i), (2 * j + 2 - i)]

      if children[1] >= len(array):
        children.pop(1)

      greatest_child_index = children[0] if (
        len(children) < 2 or array[children[0]] > array[children[1]]
      ) else children[1]

      greatest_child = array[greatest_child_index]

      if greatest_child > array[j]:
        array[j], array[greatest_child_index] = array[greatest_child_index], array[j]

  return array[::-1]


if __name__ == "__main__":
  print(heap_sort(
    [8, 5, 2, 9, 5, 6, 3]
  ))