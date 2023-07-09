"""
Write a function that takes a list of unordered positive integers and returns the majority element in the list.

TC: O(n)
SC: O(1)
"""
def majority_element(array):
  i = last_element = 0
  while i < len(array) / 2:
    counter, element = 0, array[i]
    if not element == last_element:
      for j in range(i, len(array)):
        counter = counter + 1 if array[j] == element else counter - 1
      if counter > 0: return element
    last_element = element
    i = i + 1


if __name__ == "__main__":
  print(majority_element([1, 2, 2, 2, 1]))