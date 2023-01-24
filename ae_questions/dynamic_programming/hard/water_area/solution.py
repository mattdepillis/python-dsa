"""
Given an array of non-neg integers in which each int = height of a pillar of width = 1, write a function that determines the area of water that would be trapped between the pillars if it were to be poured over the top.

NOTE: this solution passes all AE test cases but has a logical flaw due to which the last edge case below (which I created independently) does not pass. This is addressed in solution 2.

TC: O(n)
SC: O(1)
"""
def water_area(heights):
  last, last_index = None, 0
  max = max_index = total_pole_height = highest_since_max = 0
  area = temp_area = 0

  for i in range(len(heights)):
    height = heights[i]

    if height:
      if height >= max:
        area, temp_area = area + (max * (i - max_index - 1)) - total_pole_height, 0
        max, max_index = height, i
        temp_area = total_pole_height = highest_since_max = 0
      else:
        if heights[i - 1] >= height: temp_area += 0
        else:
          if height >= highest_since_max:
            temp_area = height * (i - max_index - 1) - total_pole_height
            highest_since_max = height
          else: temp_area += min(last, height) * (i - last_index - 1)
        total_pole_height += height
      last, last_index = height, i
    
  return area + temp_area


if __name__ == "__main__":
  # print(water_area([0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]))
  # print(water_area([0, 8, 0, 0, 10, 0, 0, 10, 0, 0, 1, 1, 0, 3]))
  # print(water_area([0, 100, 0, 0, 10, 1, 1, 10, 1, 0, 1, 1, 0, 0])) # 39
  print(water_area([0, 100, 0, 0, 10, 1, 1, 10, 1, 0, 1, 0, 0, 2, 0])) # 46