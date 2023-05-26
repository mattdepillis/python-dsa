"""

"""
def find_val(array, r, pos):
  print("r:", r)
  if pos:
    i, m = None, float('-inf')
    for idx in r: (i, m) = (idx, array[idx]) if array[idx] > m else (i, m)
  else:
    i, m = None, float('inf')
    for idx in r:
      print(array[idx], array[idx] < m)
      (i, m) = (idx, array[idx]) if array[idx] < m else (i, m)
  return i, m

def extend_expression(array, sum, start, remaining):
  print(f"""
    array: {array},
    sum: {sum},
    start: {start},
    remaining: {remaining}
  """)

  # keep track of index and value
  to_add = remaining % 2 == 0

  possible_values = range(start, len(array) - remaining + 1)
  if len(possible_values) == remaining:
    i = possible_values[0]
    val = array[i]
  else:
    i, val = find_val(array, possible_values, True) if to_add else find_val(array, possible_values, False)

  print(f"i: {i}, val: {val}")

  sum = sum + val if to_add else sum - val

  return extend_expression(array, sum, i + 1, remaining - 1) if remaining > 1 else sum

def maximize_expression(array):
  max_exp = 0
  if len(array) < 4: return max_exp

  return extend_expression(array, max_exp, 0, 4)


if __name__ == "__main__":
  # print(maximize_expression(
  #   [3, 6, 1, -3, 2, 7]
  # )) # 4

  print(maximize_expression(
    [6, 2, 3, 4, 1, -1, -2, 3, 1, 7, 8, -8, 2, 5, 1]
  ))