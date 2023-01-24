"""
Given an array of non-neg integers in which each int = height of a pillar of width = 1, write a function that determines the area of water that would be trapped between the pillars if it were to be poured over the top.
"""

"""
Most efficient water_area algorithm.
Uses a 2-pointer strategy to iterate forward and backward through the array simultaneously.
When the left pointer >= right pointer, break.
Use the if-else condition to arbitrarily move the pointers forward/backward.
Each time the pointer is moved, reevaluate the left or right maximum value and add max - height at the l/r index to area.

TC: O(n) -- must iterate through the entire array length
SC: O(1) -- don't need to create a holding array for left and right max values
"""
def optimal_water_area(heights):
  left, right = 0, len(heights) - 1
  left_max, right_max = heights[left], heights[right]
  area = 0

  while left < right:
    if heights[left] < heights[right]:
      left += 1
      left_max = max(left_max, heights[left])
      area += left_max - heights[left]
    else:
      right -= 1
      right_max = max(right_max, heights[right])
      area += right_max - heights[right]

  return area

"""
A less optimal water_area algorithm that satisfies all use cases and preps for understanding the optimal algorithm.
Creates an array of maxes and fills it with the max preceding column height at each index.
Then, resets the value at each index in maxes to:
  - 0 if the height at column i is greater than the min of the current left and right max values there
  - min(left and right max) - column height otherwise

TC: O(n) -- must iterate through heights twice and maxes once to sum values
SC: O(n) -- must create an array n items long to hold the left maxes -> water areas at each index
"""
def water_area(heights):
  maxes = [0 for _ in heights]

  left_max = right_max = 0
  for i in range(len(heights)):
    maxes[i] = left_max
    left_max = max(left_max, heights[i])

  for i in reversed(range(len(heights))):
    """
    ? maxes[i] is the left_max at this i
    * the amount of water area at index i is 0 if smaller_max between left and right max at this index is bigger than the height of the pillar at i
    * else, is smaller_max - height of pillar at i
    """
    smaller_max = min(right_max, maxes[i])
    maxes[i] = 0 if heights[i] > smaller_max else smaller_max - heights[i]
    right_max = max(right_max, heights[i])

  return sum(maxes)

if __name__ == "__main__":
  # print(water_area([0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]))
  # print(water_area([0, 8, 0, 0, 10, 0, 0, 10, 0, 0, 1, 1, 0, 3]))
  # print(water_area([0, 100, 0, 0, 10, 1, 1, 10, 1, 0, 1, 1, 0, 0])) # 39
  # print(water_area([0, 100, 0, 0, 10, 1, 1, 10, 1, 0, 1, 0, 0, 2, 0])) # 46
  print(water_area([4, 0, 1, 0, 6, 0, 3])) # 14