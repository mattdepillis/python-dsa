"""
Given a non-empty array of positive integers, which represent the amount of time specific queries take to execute, write a function that returns the minimum total waiting time.
"""
def minimum_wait_time(array):
  array.sort()
  min_time = sum = 0

  for item in array:
    min_time += sum
    sum += item

  return min_time


if __name__ == "__main__": # 1, 2, 2, 3, 6
  print(minimum_wait_time([3, 2, 1, 2, 6])) # 0 + 1 + 3 + 5 + 8