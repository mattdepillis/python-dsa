"""
Write a function that takes in two strings and returns the minimum number of edit operations that need to be performed on the first string to obtain the second.

3 operations:
1) insert char,
2) delete char,
3) substitute chars

TC:
SC:
"""

# optimal TC: O(n*m)
# optimal SC: O(min(n, m))
def levenshtein_distance(s1, s2):
  operations, list_s1 = (abs(len(s1) - len(s2))), list(s1)
  print('operations', operations)

  for char in s2:
    for i in range(len(list_s1)):
      if list_s1[i] == char:
        list_s1.pop(i)
        break

  return operations + len(list_s1)


if __name__ == "__main__":
  # print(levenshtein_distance("cereal", "saturday"))
  # print(levenshtein_distance("biting", "mitten"))
  print(levenshtein_distance("cereal", "saturdzz"))