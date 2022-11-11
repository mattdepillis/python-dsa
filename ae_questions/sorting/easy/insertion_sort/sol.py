"""
Insertion sort review.
"""
# def insertion_sort(array):
#   if len(array) < 2: return array

#   for i in range(1, len(array)):
#     num_sorted = False
#     while i > 0 and not num_sorted:
#       if array[i] < array[i - 1]:
#         array[i - 1], array[i] = array[i], array[i - 1]
#         i -= 1
#       else:
#         num_sorted = True

#   return array

def insertion_sort(array):
  # for-loop is skipped if len(array) < 2
  for i in range(1, len(array)):
    current = array[i]
    while i > 0 and current < array[i - 1]:
      array[i - 1], array[i] = array[i], array[i - 1]
      i -= 1

  return array


if __name__ == "__main__":
  print(insertion_sort(
    [8, 5, 2, 9, 5, 6, 3]
  ))