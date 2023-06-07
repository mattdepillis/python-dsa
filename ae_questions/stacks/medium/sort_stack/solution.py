"""
Write a function that takes in a stack and recursively sorts the stack in place. Only use the .pop() and .append() native list methods to achieve this. NOTE: the top of the stack is the end of the list.

TC: O(n^2) - we loop through the list to find the current max value about n times
SC: O(n) - maximum depth of recursion is equal to n elements
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