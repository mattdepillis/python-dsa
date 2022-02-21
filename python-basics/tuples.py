"""
  1. Write a function that takes a pair of tuples that each represent a complex number,
  and returns the sum of those complex numbers.
"""
def add_complex_numbers(cnum1, cnum2):
  (a, b), (c, d) = cnum1, cnum2
  ac = int(a) + int(c)
  bd = str(int(b[:len(b) - 1]) + int(d[:len(d) - 1])) + 'i'
  print(bd)
  return "{} + {}".format(ac, bd)


###################################################################################################################################
"""
  2. Flatten a tuple with nested tuples by printing in sequential order.
"""
nested_tuple = ( 1, 2, ( 3, 4 ), 5, ( ( 6, 7, 8, ( 9, 10 ), 11 ), 12, 13 ), ( ( 14, 15, 16 ), ( 17, 18, 19, 20 ) ) )

def flatten_tuple(t):
  for i in range(len(t)):
    if (isinstance(t[i], tuple)):
      flatten_tuple(t[i])
    else:
      print(t[i])

flatten_tuple(nested_tuple)