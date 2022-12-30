"""


"""
# def evaluate_num(num, ranges, longest):
#   if not len(ranges) or not num == ranges[-1][-1] + 1:
#     ranges += [[num, num]]
#   else: ranges[-1][1] = num

#   range_diff = ranges[-1][1] - ranges[-1][0]
#   if range_diff > longest[0]:
#     longest = [range_diff, ranges[-1]]
#   return longest

# def largest_range(array):
#   neg, pos = set({x for x in array if x < 0}), set({x for x in array if x >= 0})
#   ranges, longest = [], [0, []]

#   print(neg, '\n', pos)

#   for num in neg: longest = evaluate_num(num, ranges, longest)
#   print(longest)
#   for num in pos: longest = evaluate_num(num, ranges, longest)
  
#   return longest[1]

def largest_range(array):
  return array


if __name__ == "__main__":
  # print(largest_range([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]))
  # print(largest_range([1, 1, 1, 3, 4]))
  # print(largest_range([0, 9, 19, -1, 18, 17, 2, 10, 3, 12, 5, 16, 4, 11, 8, 7, 6, 15, 12, 12, 2, 1, 6, 13, 14, -23]))
  print(largest_range([-7, -7, -7, -7, 8, -8, 0, 9, 19, -1, -3, 18, 17, 2, 10, 3, 12, 5, 16, 4, 11, -6, 8, 7, 6, 15, 12, 12, -5, 2, 1, 6, 13, 14, -4, -2]))