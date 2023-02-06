"""

"""
# def stack_disks(disks, stack):
#   smallest = [disks[0]] if not len(stack) else stack[0]
#   for i in range(len(disks)):
    

def disk_stacking(disks):
  stack, max_height = [], 0
  for i in range(len(disks)):
    s = [[disks[i]]]
    for j in range(len(disks)):
      greater = True
      for d in range(len(disks[i])):
        if not disks[j][d] > s[0][len(s[0]) - 1][d]: greater = False
      if greater: s[0].append(disks[j])
    # print(f"disks[i]: {disks[i]}, s: {s}")
    height = 0
    for i in range(len(s[0])):
      height += s[0][i][2]
    # print(f"disks[i]: {disks[i]}, height: {height}")
    if height > max_height: max_height, stack = height, s[0]

  return stack


if __name__ == "__main__":
  print(disk_stacking([
    [2, 1, 2], # width, depth, height
    [3, 2, 3],
    [2, 2, 8],
    [2, 3, 4],
    [1, 3, 1],
    [4, 4, 5]
  ]))
