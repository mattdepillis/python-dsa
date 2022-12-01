"""
Write a function that, given 2 positive integers representing the height and width of a graph, returns the number of ways to reach the bottom right corner of the graph when starting at the top left. All moves must be down and right.

TC: O(n * m) -- proportional to m * n even though it won't quite reach m * n matrix operations
SC: O(n * m) -- need to create a matrix of m * n size
"""

# solution 1
def num_ways_to_traverse_graph(width, height):
  matrix = [ [1 for _ in range(width)] for _ in range(height) ]

  for i in range(1, height):
    for j in range(1, width):
      matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]

  return matrix[-1][-1]


if __name__ == "__main__":
  print(num_ways_to_traverse_graph(2, 2)) # 2
  print(num_ways_to_traverse_graph(2, 3)) # 3
  print(num_ways_to_traverse_graph(4, 4)) # 3