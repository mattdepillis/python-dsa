"""
1
"""
def interweaving_strings(one, two, three):
  if len(three) == 0: return True
  longer, shorter = (one, two) if len(one) >= len(two) else (two, one)
  recurse = None
  if len(longer) and longer[0] == three[0]: recurse = 'one' if longer == one else 'two'
  elif len(shorter) and shorter[0] == three[0]: recurse = 'one' if shorter == one else 'two'

  if recurse:
    # print('here: ', recurse, one, two, three)
    i = interweaving_strings(one[1:], two, three[1:]) if recurse == 'one' else interweaving_strings(one, two[1:], three[1:])
    return i
  return False


def interweaving_strings_2(one, two, three):
  if len(three) == 0: return True

  ct_one = ct_two = 0
  matched_one = matched_two = True

  while matched_one and matched_two:
      i = max(ct_one, ct_two)
      matched_one, ct_one = (True, ct_one + 1) if len(one) > i and one[i] == three[i] else (False, ct_one)
      matched_two, ct_two = (True, ct_two + 1) if len(two) > i and two[i] == three[i] else (False, ct_two)

  if max(ct_one, ct_two) <= 0: return False
  
  longer, shorter = (one, two) if ct_one >= ct_two else (two, one)
  jump = max(ct_one, ct_two)

  print(f"three: {three}, longer: {longer}, shorter: {shorter}, jump: {jump}")

  return interweaving_strings_2(longer[jump:], shorter, three[jump:])



if __name__ == "__main__":
  # print(interweaving_strings(
  #   "algo",
  #   "frog",
  #   "fralgogo"
  # )) # True

  # print(interweaving_strings(
  #   "a",
  #   "b",
  #   "ac"
  # ))

  # print(interweaving_strings_2(
  #   "aacaaaa",
  #   "aaabaaa",
  #   "aaaabacaaaaaaa"
  # )) # True

  # print(interweaving_strings_2(
  #   "ae",
  #   "e",
  #   "see"
  # )) # False

  # print(interweaving_strings(
  #   "aacaaaa",
  #   "aaabaaa",
  #   "aaaacabaaaaaaa"
  # ))

  print(interweaving_strings(
    "aacaaaa",
    "aaabaaa",
    "aaaabacaaaaaaa"
  )) # True