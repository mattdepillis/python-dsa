"""
Write a function that takes in an array of >= 3 ints and, without sorting the input array, returns a sorted array of the three largest integers in the input array.
"""
def find_three_largest_nums(list):
  num1, num2, num3 = float('-inf'), float('-inf'), float('-inf')
  for num in list:
    if num > num3:
      num3, num2, num1 = num, num3, num2
    elif num > num2:
      num2, num1 = num, num2
    elif num > num1:
      num1 = num
  return [num1, num2, num3]

if __name__ == '__main__':
  print(find_three_largest_nums([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]))
  print(find_three_largest_nums([10, 5, 9, 10, 12]))