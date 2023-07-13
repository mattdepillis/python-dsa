"""

"""
def sweet_and_savory(array, target):
  sweet, savory, ideal = [], [], [0, 0]
  for item in array:
    if item < 0: sweet.append(item)
    else: savory.append(item)
    
  for sw in sweet:
    for sa in savory:
      combo = sw + sa
      if combo <= target and (combo >= sum(ideal) or ideal == [0, 0]):
        ideal = [sw, sa]
  return ideal


if __name__ == "__main__":
  print(sweet_and_savory([-3, -5, 1, 7], 8)) # [-3, 7]

  print(sweet_and_savory([3, 5, 7, 2, 6, 8, 1], 10)) # [0, 0]

  print(sweet_and_savory([2, 5, -4, -7, 12, 100, -25], -20)) # [5, -25]