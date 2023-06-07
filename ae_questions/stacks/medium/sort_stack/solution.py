"""

"""
def handle_recursive_stack_sort(stack):
  if len(stack) < 2: return stack
  max_val, max_idx = stack[0], 0

  for i in range(1, len(stack)):
    if stack[i] > max_val: max_val, max_idx = stack[i], i

  stack.pop(max_idx)
  stack = handle_recursive_stack_sort(stack)
  stack.append(max_val)
  return stack

def sort_stack(stack):
  return handle_recursive_stack_sort(stack)


if __name__ == "__main__":
  print(sort_stack(
    [0, -2, 3, 4, 1, -9, 8]
  ))