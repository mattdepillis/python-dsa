"""

"""
def find_val(array, r, pos):
  if pos:
    i, m = None, float('-inf')
    for idx in r: i, m = idx, array[idx] if array[idx] > m else i, m
  else:
    i, m = None, float('inf')
    for idx in r: i, m = idx, array[idx] if array[idx] < m else i, m
  return i, m

def extend_expression(array, sum, start, remaining):
  # keep track of index and value

  possible_values = range(start, len(array) - remaining)
  if len(possible_values) == remaining:
    i = possible_values[0]
    val = array[i]
  else:
    i, val = find_val(array, possible_values, True) if remaining % 2 == 0 else find_val(array, possible_values, False)

  

  return possible_values

def maximize_expression(array):
  max_exp = 0
  if len(array) < 4: return max_exp

  return extend_expression(array, max_exp, 0, 4)


if __name__ == "__main__":
  print(maximize_expression(
    [3, 6, 1, -3, 2, 7]
  )) # 4