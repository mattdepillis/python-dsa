"""
Given a list of intervals (provided in start, end pairs in sublists), return a new list of the intervals from that list that intersect.
"""
def merge_overlapping_intervals(intervals):
  overlapping, sorted = [], []

  intervals.sort()

  for i in range(len(intervals)):
    for num in intervals[i]:
      if i > 0 and num <= sorted[-1]:
        if intervals[i - 1] not in overlapping: overlapping.append(intervals[i - 1])
        if overlapping[-1] != intervals[i]: overlapping.append(intervals[i])
      sorted.append(num)
      sorted.sort()

  return overlapping


if __name__ == "__main__":
  print(merge_overlapping_intervals([
    [1, 2], [3, 5], [4, 7], [6, 8], [9, 10]
  ]))

  print(merge_overlapping_intervals([
    [89, 90], [-10, 20], [-50, 0], [70, 90], [90, 91], [90, 95]
  ]))