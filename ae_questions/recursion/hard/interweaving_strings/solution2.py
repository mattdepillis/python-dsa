"""
Write a function that takes in three strings and returns a boolean representing whether or not the third string can be formed by interweaving the first two strings. Letters within a string should maintain their relative ordering in the interwoven string.

NOTE: this is the optimal solution to the problem. This solution uses a cache to store prior values of T/F depending on whether or not the string is the interwoven combo of the first two. Therein lies the tradeoff -- more memory used to avoid applying more recursive operations.

TC: O(n * m) -- worst-case, the function could approach n * m recursive calls (if condition 1 returns False almost every time in the recursive call, and the second if-condition must continually be evaluated)
SC: O(n * m) -- uses a cache of size n * m to keep track of prior results.
"""
def are_interwoven(one, two, three, o, t, cache):
  if cache[o][t] is not None: return cache[o][t]
  c = o + t
  if c == len(three): return True

  """
  - If there are still remaining letters to check in one and current index in one == curr in three, keep recursing
  - if we end up with a False value, try the same strategy with two
  - if False at any point along the way, will just backtrack letters and try 2nd-if-cond if not tried for that o/t combo yet
  """

  if o < len(one) and one[o] == three[c]:
    # print("one", o, t)
    cache[o][t] = are_interwoven(one, two, three, o + 1, t, cache)
    # print('\n', f"in one pod -- o: {o}, t: {t}", '\n', cache)
    if cache[o][t]: return True

  if t < len(two) and two[t] == three[c]:
    # print("two", o, t)
    cache[o][t] = are_interwoven(one, two, three, o, t + 1, cache)
    # print('\n', f" in two pod -- o: {o}, t: {t}", '\n', cache)
    return cache[o][t]

  cache[o][t] = False
  # print('\n', f"at end -- o: {o}, t: {t}", '\n', cache)
  return False


def interweaving_strings(one, two, three):
  if not len(three) == len(one) + len(two): return False
  """
  the cache keeps track of T/F at a given index combination of one and two
  if we return to an index that's False or True, we know not to continue recursing; rather, return that boolean val
  """
  cache = [[None for _ in range(len(two) + 1)] for _ in range(len(one) + 1)]
  return are_interwoven(one, two, three, 0, 0, cache)


if __name__ == "__main__":
  print(interweaving_strings(
    "aacaaaa",
    "aaabaaa",
    "aaaacabaaaaaaa"
  ))