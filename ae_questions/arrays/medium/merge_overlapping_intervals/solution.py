"""
Given a list of intervals (provided in start, end pairs in sublists), return a new list of the intervals from that list that intersect.
"""
def merge_overlapping_intervals(intervals):
  merged = []

  intervals.sort()

  for i in range(len(intervals)):
    if i > 0 and intervals[i][0] <= merged[-1][1]:
      if intervals[i][1] > merged[-1][1]: merged[-1][1] = intervals[i][1]
      continue
    merged.append(intervals[i])

  return merged


if __name__ == "__main__":
  # print(merge_overlapping_intervals([
  #   [1, 2], [3, 5], [4, 7], [6, 8], [9, 10]
  # ]))

  # print(merge_overlapping_intervals([
  #   [89, 90], [-10, 20], [-50, 0], [70, 90], [90, 91], [90, 95]
  # ]))

  print(merge_overlapping_intervals([
    [1, 22],
    [-20, 30]
  ]))