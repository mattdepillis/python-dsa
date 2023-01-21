"""
"""
def water_area(heights):
  direction = None
  poles = [None, None]
  spaces = 0
  max = max_index = total_pole_height = 0
  area = temp_area = 0

  for i in range(len(heights)):
    height = heights[i]
    spaces += 1 

    if height:
      if height > max:
        print('max switch!')
        max, max_index = height, i
      poles[0], poles[1] = height, poles[0]

      d = "increasing" if not poles[1] or poles[0] >= poles[1] else "decreasing"
      if d != direction: spaces = 0
      direction = d

    print(f"i: {i}, height:{height}, direction: {direction}, spaces: {spaces}, max: {max}, max_index: {max_index}")
    

  return heights


if __name__ == "__main__":
  print(water_area([0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]))