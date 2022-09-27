"""
Write an algorithm that determines whether or not an array represents a single-cycle graph. The length of the array represents the number of nodes in the graph. A positive value for any given array item means the graph is advancing forward x number of nodes that move, whereas a negative number represents x number of moves backward in the graph. For example, ```is_single_cycle([2, 3, 1, -4, -4, 2]``` should return ```True```.

TC: O(n), SC: O(1)
"""
def is_single_cycle(array):
  counter, length = 0, len(array)
  pos, neg = 0, 0
  for item in array:
    counter += item
    (pos, neg) = (pos + item, neg) if item >= 0 else (pos, neg - item)
  return counter % length == 0 and (abs(pos) >= length or abs(neg) >= length)


if __name__ == "__main__":
  print(is_single_cycle([2, 3, 1, -4, -4, 2]))