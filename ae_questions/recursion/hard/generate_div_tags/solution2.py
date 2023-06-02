"""
"""
def wrap(string):
  return "<div>" + string + "</div>"

def generate_new_tag_combos(string):
  return [
    wrap(string), # wrap
    "<div></div>" + string, # prepend
    string + "<div></div>" # append
  ]

def generate_two_tag_combos(string1, string2):
  return [
    string1 + string2,
    string2 + string1
  ]

def recurse(tags):
  if tags == 1: return { 1: [ "<div></div>" ] }
  valid = set()
  prior_valid = recurse(tags - 1)

  # for tag_level in prior_valid:
  for combo in prior_valid[tags - 1]:
    new_combos = generate_new_tag_combos(combo)
    for nc in new_combos:
      valid.add(nc)

  # generate the missing combinations from prior valid tag levels
  tried = set()
  r = reversed(range(2, tags - 1))
  for i in r:
    if i in tried: continue
    tags_i, tags_j = prior_valid[i], prior_valid[tags - i]
    for valid_i in tags_i:
      for valid_j in tags_j:
        nc = generate_two_tag_combos(valid_i, valid_j)
        for s in nc: valid.add(s)

  prior_valid[tags] = list(valid)
  
  return prior_valid

def generate_div_tags(tags):
  return recurse(tags)[tags]


if __name__ == "__main__":
  # mine = generate_div_tags(5)
  mine = generate_div_tags(4)
  print(len(mine))