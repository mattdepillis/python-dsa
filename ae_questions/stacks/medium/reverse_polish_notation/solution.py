"""

"""
def is_operator(element):
  return element in [ "+", "-", "*", "/" ]

def perform_operation(num1, num2, operation):
  if operation == "+": return num1 + num2
  elif operation == "-": return num1 - num2
  elif operation == "*": return num1 * num2
  else: return num1 // num2

def reverse_polish_notation(tokens):
  stack = []

  for element in tokens:
    if is_operator(element):
      first, second = stack.pop(len(stack) - 2), stack.pop(len(stack) - 1)
      element = perform_operation(int(first), int(second), element)
    stack.append(element)

  return stack[0]


if __name__ == "__main__":
  print(reverse_polish_notation(
    ["50", "3", "17", "+", "2", "-", "/"] # 2
  ))