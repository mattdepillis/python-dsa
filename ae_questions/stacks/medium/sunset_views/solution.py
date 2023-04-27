"""

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