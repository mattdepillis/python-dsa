"""

"""
def disk_stacking(disks):
  disks.sort()
  stack, max_height = [], 0
  for i in range(len(disks)):
    s = [[disks[i]]]
    for j in range(len(disks)):
      greater = True
      for d in range(len(disks[i])):
        if not disks[j][d] > s[0][len(s[0]) - 1][d]: greater = False
      if greater: s[0].append(disks[j])
    height = 0
    for i in range(len(s[0])):
      height += s[0][i][2]
    if height > max_height: max_height, stack = height, s[0]

  return stack


if __name__ == "__main__":

  # disks = [
  #   [2, 1, 2], # width, depth, height
  #   [3, 2, 3],
  #   [2, 2, 8],
  #   [2, 3, 4],
  #   [1, 3, 1],
  #   [4, 4, 5]
  # ]

  disks = [
    [3, 3, 4],
    [2, 1, 2],
    [3, 2, 3],
    [2, 2, 8],
    [2, 3, 4],
    [5, 5, 6],
    [1, 2, 1],
    [4, 4, 5],
    [1, 1, 4],
    [2, 2, 3]
  ]

  print(disk_stacking(disks))
