"""

"""
def generate_new_tag_combos(string):
  return [
    "<div>" + string + "</div>", # wrap
    "<div></div>" + string, # prepend
    string + "<div></div>" # append
  ]

def recurse(tags):
  if tags == 1: return [ "<div></div>" ]
  valid, prior_valid = set(), recurse(tags - 1)
  for combo in prior_valid:
    new_combos = generate_new_tag_combos(combo)
    for nc in new_combos:
      if nc in valid: continue
      valid.add(nc)
  return list(valid)

def generate_div_tags(tags):
  return recurse(tags)


if __name__ == "__main__":
  print(generate_div_tags(3))