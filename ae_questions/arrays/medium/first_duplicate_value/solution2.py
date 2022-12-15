"""
Given an array of integers with values between 1 and n, where n is the length of the array, write a function that returns the first integer that appears more than once.

TC: O(n)
SC: O(1)
"""
def first_duplicate_value(array):
  """
  For each value in the array, calculate its absolute value (which is equal to its positive starting value).
  A unique value (for example, 2) should always yield the same index to check (av - 1).

  Since all the numbers in the array start positive and between the values of 1 and n,
  we can tell if a number has been encountered twice if the number at the index to check has been turned negative.
  """
  for item in array:
    av = abs(item)
    if array[av - 1] < 0:
      return av
    array[av - 1] *= -1
  return -1


if __name__ == "__main__":
  """
  In this example, after the first item (2), the array looks like the following:
    ```[2, -1, 5, 2, 3, 3, 2, 4]```
  as 2 - 1 yields 1 and array[1] is not < 0.

  The next time we check 2, we again must check 2 - 1 = index 1, and since array[1] is negative, we return the av (2).
  """
  print(first_duplicate_value([2, 1, 5, 2, 3, 3, 2, 4]))