"""
Write a function that takes a list of integers and returns a list of the same length, for which the value at each index in the list is the product of all the numbers not at that same index in the input list.

TC: O(n) -- iterate through the products array 2 separate times, front to back and then back to front
SC: O(n) -- return a list equal in size to the input list
"""
def multiply(list, products, reverse):
  multiplier = 1
  r = reversed(range(len(list))) if reverse else range(len(list))
  for i in r:
    products[i] *= multiplier
    multiplier *= list[i]


def array_of_products(list):
  products = [1 for _ in list]

  multiply(list, products, False)
  multiply(list, products, True)

  return products


if __name__ == "__main__":
  print(array_of_products([5, 1, 4, 2])) # [8, 40, 10, 20]