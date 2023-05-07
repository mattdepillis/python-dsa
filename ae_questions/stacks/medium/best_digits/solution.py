"""

"""
def find_max_and_index(stack_subset):
  max = idx = -1
  for i in range(len(stack_subset)):
    if stack_subset[i] > max:
      max, idx = stack_subset[i], i
  return max, idx

def best_digits(number, remove):
  shortened, stack = "", [int(char) for char in number]
  digits_to_add = len(stack) - remove

  while digits_to_add > 0 and digits_to_add < len(stack):
    last_potential_index = len(stack) - digits_to_add + 1
    max, idx = find_max_and_index(stack[:last_potential_index])
    shortened += str(max)
    for i in range(0, idx + 1):
      stack.pop(0)
    digits_to_add -= 1

  if digits_to_add > 0:
    for i in stack: shortened += str(i)

  return shortened


if __name__ == "__main__":
  print(best_digits(
    "129847563", 4
  )) # 98763

  print("\n\n")

  print(best_digits(
    "462839", 2
  )) # 6839

  print("\n\n")

  print(best_digits(
    "22", 1
  ))