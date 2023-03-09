"""
Given a string representation of the first n digits of pi, and a list of positive integers that might comprise sequences of the n pi digits, create a method that returns the smallest number of unions (spaces) between distinct matches in the n digits with an array number.

TC: hit -> shortened pi, m numbers again
SC: 
"""
def recurse(pi, numbers, spaces):
  number_in_pi, min_spaces = False, float('inf')
  for number in numbers:
    if number == pi[:len(number)]:
      number_in_pi = True
      new_pi = pi[len(number):]
      if new_pi == "": return spaces
      s = recurse(new_pi, numbers, spaces + 1)
      if s < min_spaces and s > 0: min_spaces = s
  return -1 if not number_in_pi or min_spaces == float('inf') else min_spaces

def numbers_in_pi(pi, numbers):
  return recurse(pi, numbers, spaces=0)

if __name__ == "__main__":
  # print(numbers_in_pi(
  #   "3141592653589793238462643383279",
  #   ["314159265358979323846", "26433", "8", "3279", "314159265", "35897932384626433832", "79"]
  # )) # 2

  # print(numbers_in_pi( # -1 should be correct
  #   "3141592653589793238462643383279",
  #   ["3", "141", "592", "65", "55", "35", "8", "9793", "23846264", "3832798"]
  # ))  # 3 | 141 | 592 | 65 | 35 | 8 | 9793 | 23846264 | 3 | 3 | 8 | 3 |

  # print(numbers_in_pi( # -1 should be correct
  #   "3141592653589793238462643383279",
  #   ["3", "141", "592", "65", "55", "35", "8", "9793", "23846264", "383279"]
  # )) # 3 | 141 | 592 | 65 | 35 | 8 | 9793 | 23846264 | 3 | 3 | 8 | 3 |

  # print(numbers_in_pi( # -1 should be correct
  #   "3141592653589793238462643383279",
  #   ["3", "141", "592", "65", "55", "35", "8", "9793", "2384626", "383279"]
  # )) # 3 | 141 | 592 | 65 | 35 | 8 | 9793 | 2384626

  # print(numbers_in_pi(
  #   "3141592653589793238462643383279",
  #   ["3", "314", "49", "9001", "15926535897", "14", "9323", "8462643383279", "4", "793"]
  # )) # 3

  print(numbers_in_pi(
    "3141592653589793238462643383279",
    ["3", "141", "592", "65", "55", "35", "8", "9793", "23846264", "383279"]
  ))