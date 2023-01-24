"""
Given an array of non-neg integers in which each int = height of a pillar of width = 1, write a function that determines the area of water that would be trapped between the pillars if it were to be poured over the top.

TC:
SC:
"""
# def water_area(heights):
#   left, right = 0, len(heights) - 1
#   left_max, right_max = heights[left], heights[right]
#   area = 0

#   while left < right:
#     if heights[left] < heights[right]:
#       left += 1
#       left_max = max(left_max, heights[left])
#       area += left_max - heights[left]
#     else:
#       right -= 1
#       right_max = max(right_max, heights[right])
#       area += right_max - heights[right]

#   return area

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