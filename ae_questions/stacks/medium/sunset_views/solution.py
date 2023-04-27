"""
Given an array of buildings and a direction all the buildings face + a sun is setting, return an array of indices representing the buildings in the array that can see the sunset in that given direction.

TC: O(n) - possibly reverse range, and loop through all indices once
SC: O(n) - could store a maximum of n elements in stack
"""

def sunset_views(buildings, direction):
  stack, top, r = [], None, range(0, len(buildings))
  if direction == "EAST": r = reversed(r)
  for i in r:
    if not top or buildings[i] > top:
      stack.append(i)
      top = buildings[i]

  return sorted(stack)


if __name__ == "__main__":
  print(sunset_views(
    [3, 5, 4, 4, 3, 1, 3, 2],
    "EAST"
  ))

  print(sunset_views(
    [3, 5, 4, 4, 3, 1, 3, 2],
    "WEST"
  ))