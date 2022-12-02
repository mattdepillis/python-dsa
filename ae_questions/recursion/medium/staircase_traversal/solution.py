"""
Given two positive integers representing the height of a staircase and the max number of steps you can advance up the staircase at a time, write a function that returns the number of ways in which you can advance up the staircase.

Recursive solution:
TC: somewhere between O(n * k) and O(k^n), where k is max steps and n is the total number of stairs to climb.
  - Since the for-loop must start at 1, you must travel max n levels for recursive depth, and each recursed level down there will be k executions of the for-loop. However, subtracting i from stairs_remaining for larger values of i will reduce number of recursive calls. It's not quite n * k calls however
SC: O(n) -- must store n-proportional number of recursive calls on the stack at a given time
"""
def helper(stairs_remaining, max_steps, ways):
  for i in range(1, max_steps + 1):
    if i <= stairs_remaining:
      s = stairs_remaining - i
      if s == 0: return ways + 1
      else: ways = helper(s, max_steps, ways)
  return ways

def staircase_traversal(stairs, max_steps):
  return helper(stairs, max_steps, 0)


if __name__ == "__main__":
  print(staircase_traversal(4, 2)) # 5