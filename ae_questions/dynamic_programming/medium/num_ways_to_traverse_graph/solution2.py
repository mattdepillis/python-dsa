"""
Write a function that, given 2 positive integers representing the height and width of a graph, returns the number of ways to reach the bottom right corner of the graph when starting at the top left. All moves must be down and right.

TC: O(n + m) ?
SC: O(n * m)
"""

# solution 1
def num_ways_to_traverse_graph(width, height):
  longer, shorter = (width, height) if width >= height else (height, width)


  ways = 1
  for i in range(1, shorter):
    ways += (i * (longer - 1))
    print('w', ways)

  return ways


if __name__ == "__main__":
  # print(num_ways_to_traverse_graph(2, 2)) # 2
  # print(num_ways_to_traverse_graph(2, 3)) # 3
  # print(num_ways_to_traverse_graph(4, 4)) # 3
  print(num_ways_to_traverse_graph(3, 3))