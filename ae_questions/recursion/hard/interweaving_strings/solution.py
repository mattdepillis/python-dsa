"""
1
"""
def interweaving_strings(one, two, three):
  if len(three) == 0: return True
  longer, shorter = (one, two) if len(one) >= len(two) else (two, one)
  recurse = None
  if longer[0] == three[0]: recurse = 'one' if longer == one else 'two'
  elif shorter[0] == three[0]: recurse = 'one' if shorter == one else 'two'

  if recurse:
    print('here: ', recurse, one, two, three)
    i = interweaving_strings(one[1:], two, three[1:]) if recurse == 'one' else interweaving_strings(one, two[1:], three[1:])
    print(i)
    return i
    # if longer == one: return interweaving_strings(one[1:], two, three[1:])
    # else: return interweaving_strings()
  # elif len(one) > 0 and one[0] == three[0]:
  #   print('recursing with 1:', one[1:], two, three[1:])
  #   i = interweaving_strings(one[1:], two, three[1:])
  #   print(i)
  # elif len(two) > 0 and two[0] == three[0]:
  #   print('recursing with 2: ', one, two[1:], three[1:])
  #   i = interweaving_strings(one, two[1:], three[1:])
  #   print(i)
  return False


if __name__ == "__main__":
  print("algo",
    "frog",
    "fralgogo")
  print(interweaving_strings(
    "algo",
    "frog",
    "fralgogo"
  )) # true