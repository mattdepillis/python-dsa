"""
Write a function that takes the number n and returns the nth fibonacci number recursively.

This implementation asks the author to count 0 as the first number in the sequence; as a note, I've seen other definitions of this problem in which 1 was regarded the first num, so this solution may vary slightly from others.

sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
"""
def nth_fibonacci(n):
  if n <= 2:
    return n - 1
  return nth_fibonacci(n - 1) + nth_fibonacci(n - 2)


if __name__ == "__main__":
  print(nth_fibonacci(3))