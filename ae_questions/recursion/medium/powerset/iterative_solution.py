"""
Write a function that intakes an array of unique integers and returns its powerset.

A powerset is all of the subsets of a set X. For example, for a set X = [1, 2] its powerset is [[], [1], [2], [1, 2]].

TC: O(n * 2^n) -- must take into account appending elements to p
SC: O(2^n)
"""
def powerset(array):
  p = [[]]
  for item in array:
    for i in range(len(p)):
      subset = p[i]
      p.append(subset + [item])
  return p


if __name__ == "__main__":
  print(powerset([1, 2, 3]))