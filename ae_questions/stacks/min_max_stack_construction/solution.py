"""
Write a min-max class for a min-max stack. Methods should include:
  - peeking at the value at the top of the stack
  - retrieving min/max values in the stack
  - pushing and popping values onto/off of the stack

NOTE: this first solution will use Python's list data structure for implementation.

TC:
SC:
"""
class MinMaxStack:
  def __init__(self):
    self.min = None
    self.max = None
    self.stack = []

  def peek(self):
    return self.stack[0]

  def push(self, value):
    if self.min is None or value < self.min:
      self.min = value
    if self.max is None or value > self.max:
      self.max = value
    self.stack.insert(0, value)

  def pop(self):
    top = self.stack[0]
    self.stack.pop(0)
    self.check_min_and_max(top)
    return top

  def check_min_and_max(self, value):
    if value == self.get_min():
      self.min = min(self.stack)
    if value == self.get_max():
      self.max = max(self.stack) 

  def get_min(self):
    return self.min

  def get_max(self):
    return self.max



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