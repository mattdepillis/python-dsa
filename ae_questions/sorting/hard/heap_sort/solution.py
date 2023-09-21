"""

"""
def heap_sort(array):
  for i in range(len(array) - 1):
    first_child_index = ((len(array) - i) // 2)

    for j in reversed(range(0, first_child_index)):
      children = [(2 * j) + 1, (2 * j) + 2]

      if children[1] >= len(array):
        children.pop(1)
      
      greatest_child_index = children[0] if (
        len(children) < 2 or array[children[0]] > array[children[1]]
      ) else children[1]

      greatest_child = array[greatest_child_index]

      if greatest_child > array[j]:
        array[j], array[greatest_child_index] = array[greatest_child_index], array[j]

  return array


if __name__ == "__main__":
  print(heap_sort(
    [8, 5, 2, 9, 5, 6, 3]
  ))