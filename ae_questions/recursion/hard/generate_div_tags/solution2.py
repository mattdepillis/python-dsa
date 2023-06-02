"""
"""

# lambda functions for wrap, prepend, and append operations
wrap = lambda string : "<div>" + string + "</div>"
prepend = lambda string: "<div></div>" + string
append = lambda string: string + "<div></div>"

def generate_new_tag_combos(string):
  return [ wrap(string), prepend(string), append(string) ]

def generate_two_tag_combos(string1, string2):
  return [
    string1 + string2,
    string2 + string1
  ]

def generate_from_prior_valid_combos(prior, current, tags):
  # generate the missing combinations from prior valid tag levels
  tried = set()
  r = reversed(range(2, tags - 1))
  for i in r:
    if i in tried: continue
    tags_i, tags_j = prior[i], prior[tags - i]
    for valid_i in tags_i:
      for valid_j in tags_j:
        nc = generate_two_tag_combos(valid_i, valid_j)
        for s in nc: current.add(s)

def recurse(tags):
  if tags == 1: return { 1: [ "<div></div>" ] }
  valid = set()
  prior_valid = recurse(tags - 1)

  # for tag_level in prior_valid:
  for combo in prior_valid[tags - 1]:
    new_combos = generate_new_tag_combos(combo)
    for nc in new_combos:
      valid.add(nc)

  generate_from_prior_valid_combos(prior_valid, valid, tags)

  prior_valid[tags] = list(valid)
  
  return prior_valid

def generate_div_tags(tags):
  return recurse(tags)[tags]


if __name__ == "__main__":
  # mine = generate_div_tags(5)
  mine = generate_div_tags(4)
  print(len(mine))