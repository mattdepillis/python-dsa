"""
Write a function that takes in an array of >= 3 ints and, without sorting the input array, returns a sorted array of the three largest integers in the input array.
"""
def find_three_largest_nums(list):
  largest = [float('-inf')] * 4
  for num in list:
    largest[0] = num
    largest.sort()
  return largest[-3:]

if __name__ == '__main__':
  print(find_three_largest_nums([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]))
  print(find_three_largest_nums([10, 5, 9, 10, 12]))