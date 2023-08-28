"""

"""
def look_forward(stack, array, index, final, max_val):
  stack.append(array[index])

  if array[index] > max_val:
    max_val = array[index]
  
  iter, stack_start, stack_position = index - 1, final.index(None), len(stack) - 1
  while iter >= stack_start:
    if not final[iter]:
      stack_position -= 1
      if stack[stack_position] < array[index]:
        stack.pop(stack_position)
        final[iter] = array[index]
    iter -= 1

  return stack, final, max_val

def look_backward(stack, index, final, start_val):
  if not final[index]:
    if len(stack) == 1:
      final[index] = -1
    else:
      if stack[len(stack) - 1] < start_val: final[index] = start_val
      else: final[index] = final[0]
      stack.pop(len(stack) - 1)

  return stack, final

def next_greater_element(arr):
  final = [None for _ in arr]
  stack = []
  start_val, max_val = arr[0], float('-inf')

  for i in range(len(arr)):
    (stack, final, max_val) = look_forward(stack, arr, i, final, max_val)

  for j in reversed(range(len(final))):
    (stack, final) = look_backward(stack, j, final, start_val)

  return final


if __name__ == "__main__":
  print(next_greater_element(
    [2, 5, -3, -4, 6, 7, 2] # [5, 6, 6, 6, 7, -1, 5]
  ))

  print(next_greater_element(
    [3, 7, -3, -4, 6, 5, 2] # [7, -1, 6, 6, 7, 7, 3]
  ))