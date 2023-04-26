"""

"""
def best_seats(array):
  if not 0 in array: return -1

  index_best = array.index(0)

  curr = num_best = 0
  for i in range(index_best, len(array) - 1):
    print(f"i: {i}, curr: {curr}, num_best: {num_best}, index_best: {index_best}, ")
    if array[i] == 1: curr = 0
    elif array[i] == 0 and array[i + 1] == 0:
      curr += 1
    print(f"curr now: {curr}")
    if curr > num_best:
      num_best, index_best = curr, i
  return index_best


if __name__ == "__main__":
  # print(best_seats(
  #   [1, 0, 1, 0, 0, 0, 1]
  # ))

  print(best_seats(
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1]
  ))