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

def look_backward(stack, index, arr, final, start_val, max_val):
  if final[index] is None:
    if len(stack) == 1 or arr[index] == max_val:
      final[index] = -1
    else:
      if stack[len(stack) - 1] < start_val: final[index] = start_val
      else:
        i = 0
        while True:
          if arr[index] < final[i]:
            final[index] = final[i]
            break
          i += 1
      stack.pop(len(stack) - 1)

  return stack, final

def next_greater_element(arr):
  if len(arr) < 1: return arr
  final = [None for _ in arr]
  stack = []
  start_val, max_val = arr[0], float('-inf')

  for i in range(len(arr)):
    (stack, final, max_val) = look_forward(stack, arr, i, final, max_val)

  for j in reversed(range(len(arr))):
    (stack, final) = look_backward(stack, j, arr, final, start_val, max_val)

  return final


if __name__ == "__main__":
  print(next_greater_element(
    [2, 5, -3, -4, 6, 7, 2] # [5, 6, 6, 6, 7, -1, 5]
  ))

  print(next_greater_element(
    [3, 7, -3, -4, 6, 5, 2] # [7, -1, 6, 6, 7, 7, 3]
  ))

  print(next_greater_element(
    [1, 0, 1, 0, 1, 0, 1] # [-1, 1, -1, 1, -1, 1, -1]
  ))

  print(next_greater_element(
    [-8, -1, -1, -2, -4, -5, -6, 0, -9, -91, -2, 8]
  )) # [-1, 0, 0, 0, 0, 0, 0, 8, -2, -2, 8, -1]

  print(next_greater_element(
    [1, 2, 3, 4, 1, 2, 3, 4, -8, -7, 6, 2, 17, 2, -8, 9, 0, 2]
  )) # [2, 3, 4, 6, 2, 3, 4, 6, -7, 6, 17, 17, -1, 9, 9, 17, 2, 3]