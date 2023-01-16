"""
Write a function that takes a string full of bracket characters (as well as other optional ones) and determines whether the brackets in the string are balanced.

TC: O(n) -- must inspect each char in string
SC: O(n) -- size of stack could worst-case be as big as the string itself (if all opening brackets, for example)
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