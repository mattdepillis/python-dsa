"""

"""
def heap_sort(array):
  for i in range(len(array) - 1):
    top_of_heap = i
    last_parent_index = ((len(array) - i) // 2) - 1 + i

    for j in reversed(range(top_of_heap, last_parent_index + 1)):
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