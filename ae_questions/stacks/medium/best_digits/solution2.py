"""
Given a string representation of a positive integer, and an integer representing the number of characters to remove from the string representation, write a function that will return the largest possible value of an int with ```len(original_string) - chars_to_remove``` characters. Original ordering of the characters cannot change in the returned result.

TC: O(n) -- loops through the number just once
SC: O(n) -- create a stack of max size n

NOTE: the major change from solution 1 is the realization that we can simply append each number to the end of the stack by default. If the next number is greater than the last number(s) in the stack, it'll simply just replace it/them while the number to remove is greater than zero. Then, join the stack together.
"""
def best_digits(number, remove):
  stack = []

  for digit in number:
    while remove > 0 and len(stack) > 0 and digit > stack[-1]:
      remove -= 1
      stack.pop()
    stack.append(digit)

  while remove > 0:
    remove -= 1
    stack.pop()

  return "".join(stack)


if __name__ == "__main__":
  print(best_digits(
    "129847563", 4
  )) # 98763