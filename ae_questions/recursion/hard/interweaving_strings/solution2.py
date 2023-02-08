"""
1
"""
def are_interwoven(one, two, three, o, t, cache):
  if cache[o][t] is not None: return cache[o][t]
  c = o + t
  if c == len(three): return True

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

  cache = [[None for _ in range(len(two) + 1)] for _ in range(len(one) + 1)]
  return are_interwoven(one, two, three, 0, 0, cache)


if __name__ == "__main__":
  print(interweaving_strings(
    "aacaaaa",
    "aaabaaa",
    "aaaacabaaaaaaa"
  ))