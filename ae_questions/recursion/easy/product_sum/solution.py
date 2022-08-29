"""
Write a function that takes in an array of integers and nested arrays containing integers and other nested arrays, and returns the product sum where nested arrays are summed and then multiplied by their level of depth.
"""
def product_sum(array, depth):
  sum = 0

  for item in array:
    if isinstance(item, list):
      sum += product_sum(item, depth + 1)
    else:
      sum += item

  return sum * depth


if __name__ == "__main__":
  print(product_sum([5, 2, [7, -1], 3, [6, [-13, 8], 4]], depth=1))