"""
"""
def water_area(heights):
  direction = None
  poles = [None, None]
  spaces = 0
  max = max_index = total_pole_height = highest_since_max = 0
  area = temp_area = 0

  for i in range(len(heights)):
    height = heights[i]

    if height:
      poles[0], poles[1] = height, poles[0]
      d = "increasing" if not poles[1] or poles[0] >= poles[1] else "decreasing"

      if height >= max:
        print('max switch!')
        area, temp_area = area + (max * (i - max_index - 1)) - total_pole_height, 0
        print('a',  area,  'm', max, (max * (i - max_index - 1)), 't', total_pole_height)
        max, max_index = height, i
        spaces = temp_area = total_pole_height = highest_since_max = 0
      else:
        if heights[i - 1] >= height: temp_area += 0
        else:
          if height >= highest_since_max:
            temp_area = height * (i - max_index - 1) - total_pole_height
            highest_since_max = height
          else: temp_area += min(poles[0], poles[1]) * spaces
        total_pole_height += height
        
      if d != direction: spaces = 0
      direction = d
      spaces += 1

    print(f"i: {i}, height:{height}, direction: {direction}, spaces: {spaces}, max: {max}, max_index: {max_index}, area: {area}, temp_area: {temp_area}")
    
  return heights, area + temp_area


if __name__ == "__main__":
  # print(water_area([0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]))
  print(water_area([0, 8, 0, 0, 10, 0, 0, 10, 0, 0, 1, 1, 0, 3]))