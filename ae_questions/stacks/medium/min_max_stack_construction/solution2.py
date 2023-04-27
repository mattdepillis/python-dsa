"""
Write a min-max class for a min-max stack. Methods should include:
  - peeking at the value at the top of the stack
  - retrieving min/max values in the stack
  - pushing and popping values onto/off of the stack

NOTE: this second solution uses a second stack to keep track of min/max values at a given element in the stack.
  - when pushing a value onto the stack, save a record of the current min/max at that value
  - this results in an O(1) operation (space complexity consistent per operation), but overall more space taken up by class the larger the stack size becomes

"""
class MinMaxStack:
  def __init__(self):
    self.min_max_stack = []
    self.stack = []

  # O(1) T+S
  def peek(self):
    return self.stack[len(self.stack) - 1]

  # O(1) T+S
  def push(self, value):
    min_max = [value, value]

    if len(self.min_max_stack):
      min_max[0] = min(self.min_max_stack[-1][0], value)
      min_max[1] = max(self.min_max_stack[-1][1], value)
    self.min_max_stack.append(min_max)
    self.stack.append(value)

  # O(1) T+S
  def pop(self):
    self.min_max_stack.pop()
    return self.stack.pop()

  # O(1) T+S
  def get_min(self):
    return self.min_max_stack[-1][0]

  # O(1) T+S
  def get_max(self):
    return self.min_max_stack[-1][1]


if __name__ == "__main__":
  stack = MinMaxStack()
  stack.push(5)
  stack.push(4)
  stack.push(3)
  print('min', stack.get_min())
  stack.pop()
  print('min', stack.get_min())
  print(stack.peek())
  print(stack.stack)