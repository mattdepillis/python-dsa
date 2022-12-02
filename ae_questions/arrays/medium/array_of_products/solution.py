"""
Write a function that takes a list of integers and returns a list of the same length, for which the value at each index in the list is the product of all the numbers not at that same index in the input list.

TC: O()
SC: O()
"""
def array_of_products(list):
  products = [1 for _ in list]
  for i, v in enumerate(list):
    products = [v * val if i != j else val for j, val in enumerate(products)]
  return products


if __name__ == "__main__":
  print(array_of_products([5, 1, 4, 2])) # [8, 40, 10, 20]