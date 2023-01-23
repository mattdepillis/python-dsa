"""
"""
def water_area(heights):
  last = None
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
          else: temp_area += min(last, height)
        total_pole_height += height
        last = height
    
  return area + temp_area


if __name__ == "__main__":
  # print(water_area([0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]))
  # print(water_area([0, 8, 0, 0, 10, 0, 0, 10, 0, 0, 1, 1, 0, 3]))
  print(water_area([0, 100, 0, 0, 10, 1, 1, 10, 1, 0, 1, 1, 0, 0]))