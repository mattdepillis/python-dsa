"""


"""
def next_greater_element(arr):
  stack, final = [], [-1 for _ in arr]

  for i in range(2 * len(arr)):
    circular_index = i % len(arr)

    while len(stack) > 0 and arr[stack[len(stack) - 1]] < arr[circular_index]:
      top = stack.pop()
      final[top] = arr[circular_index]

    stack.append(circular_index)

  return final

if __name__ == "__main__":
  print(next_greater_element(
    [2, 5, -3, -4, 6, 7, 2] # [5, 6, 6, 6, 7, -1, 5]
  ))

  # print(next_greater_element(
  #   [3, 7, -3, -4, 6, 5, 2] # [7, -1, 6, 6, 7, 7, 3]
  # ))

  # print(next_greater_element(
  #   [1, 0, 1, 0, 1, 0, 1] # [-1, 1, -1, 1, -1, 1, -1]
  # ))