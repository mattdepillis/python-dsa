"""

"""
def balanced_brackets(string):
  stack, pairs, allowed = [], { "}": "{", ")": "(", "]": "[" }, set({ "{", "}", "(", ")", "[", "]" })

  for char in string:
    if char not in allowed:
      continue
    if len(stack) and char in pairs and stack[-1] == pairs[char]:
      stack.pop()
    else: stack.append(char)
  return len(stack) == 0


if __name__ == "__main__":
  print(balanced_brackets("([])(){as}(())()()"))
  print(balanced_brackets("([)]"))