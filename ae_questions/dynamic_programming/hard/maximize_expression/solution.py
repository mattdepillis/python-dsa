"""
Write a function that takes an array of integers and returns the largest possible value for the following expression:
```
array[a] - array[b] + array[c] - array[d]
```,
where a < b < c < d.

TC: O(n) - loop through elements once.
SC: O(n) - store max state for 1-4 number sums in a matrix of 4 rows and n cols.
"""
def determine_sign(number, row):
  return number if row % 2 == 0 else number * -1

def maximize_expression(array):
  if len(array) < 4: return 0
  matrix = [[None for _ in range(len(array))] for _ in range(4)]
  matrix[0][0] = array[0]

  for col in range(1, len(array)):
    for row in range(0, min(col + 1, 4)):
      prev = matrix[row][col - 1]
      one_less_max = 0 if row == 0 else matrix[row - 1][col - 1]
      if prev is None:
        matrix[row][col] = one_less_max + determine_sign(array[col], row)
      else:
        if row == 0: matrix[row][col] = max(prev, array[col])
        else:
          matrix[row][col] = max(prev, one_less_max + determine_sign(array[col], row))
    
  return matrix[-1][-1]

if __name__ == "__main__":
  print(maximize_expression(
    [3, 6, 1, -3, 2, 7]
  )) # 4

  print(maximize_expression(
    [6, 2, 3, 4, 1, -1, -2, 3, 1, 7, 8, -8, 2, 5, 1]
  ))