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

def recurse(tags):
  if tags == 1: return [ "<div></div>" ], { 1: "<div></div>" }
  valid = set()
  prior_valid, wrapped = recurse(tags - 1)

  print('w', wrapped)

  for key in wrapped.keys():
    if tags % key == 0:
      print('k', key, 't', tags, wrapped[key] * (tags // key))
      valid.add(wrapped[key] * (tags // key))

  wrapped[tags] = wrap(wrapped[tags - 1])

  print('v', valid)

  for combo in prior_valid:
    new_combos = generate_new_tag_combos(combo)
    for nc in new_combos:
      valid.add(nc)
  
  return list(valid), wrapped

def generate_div_tags(tags):
  t = recurse(tags)
  return t


if __name__ == "__main__":
  mine = generate_div_tags(5)
  # mine = generate_div_tags(4)
  print('w *** ', mine[1])
  print(len(mine[0]))

  # correct_4 = [
  #   "<div><div><div><div></div></div></div></div>", "<div><div><div></div><div></div></div></div>", "<div><div><div></div></div><div></div></div>", "<div><div><div></div></div></div><div></div>", "<div><div></div><div><div></div></div></div>", "<div><div></div><div></div><div></div></div>", "<div><div></div><div></div></div><div></div>", "<div><div></div></div><div><div></div></div>", "<div><div></div></div><div></div><div></div>", "<div></div><div><div><div></div></div></div>", "<div></div><div><div></div><div></div></div>", "<div></div><div><div></div></div><div></div>", "<div></div><div></div><div><div></div></div>", "<div></div><div></div><div></div><div></div>"
  # ]
  # # print(len(correct_4))

  # missing = [tag for tag in correct_4 if tag not in mine[0]]
  # print(missing)

  # mine = generate_div_tags(5)

  correct_5 = [
    "<div><div><div><div><div></div></div></div></div></div>", "<div><div><div><div></div><div></div></div></div></div>", "<div><div><div><div></div></div><div></div></div></div>", "<div><div><div><div></div></div></div><div></div></div>", "<div><div><div><div></div></div></div></div><div></div>", "<div><div><div></div><div><div></div></div></div></div>", "<div><div><div></div><div></div><div></div></div></div>", "<div><div><div></div><div></div></div><div></div></div>", "<div><div><div></div><div></div></div></div><div></div>", "<div><div><div></div></div><div><div></div></div></div>", "<div><div><div></div></div><div></div><div></div></div>", "<div><div><div></div></div><div></div></div><div></div>", "<div><div><div></div></div></div><div><div></div></div>", "<div><div><div></div></div></div><div></div><div></div>", "<div><div></div><div><div><div></div></div></div></div>", "<div><div></div><div><div></div><div></div></div></div>", "<div><div></div><div><div></div></div><div></div></div>", "<div><div></div><div><div></div></div></div><div></div>", "<div><div></div><div></div><div><div></div></div></div>", "<div><div></div><div></div><div></div><div></div></div>", "<div><div></div><div></div><div></div></div><div></div>", "<div><div></div><div></div></div><div><div></div></div>", "<div><div></div><div></div></div><div></div><div></div>", "<div><div></div></div><div><div><div></div></div></div>", "<div><div></div></div><div><div></div><div></div></div>", "<div><div></div></div><div><div></div></div><div></div>", "<div><div></div></div><div></div><div><div></div></div>", "<div><div></div></div><div></div><div></div><div></div>", "<div></div><div><div><div><div></div></div></div></div>", "<div></div><div><div><div></div><div></div></div></div>", "<div></div><div><div><div></div></div><div></div></div>", "<div></div><div><div><div></div></div></div><div></div>", "<div></div><div><div></div><div><div></div></div></div>", "<div></div><div><div></div><div></div><div></div></div>", "<div></div><div><div></div><div></div></div><div></div>", "<div></div><div><div></div></div><div><div></div></div>", "<div></div><div><div></div></div><div></div><div></div>", "<div></div><div></div><div><div><div></div></div></div>", "<div></div><div></div><div><div></div><div></div></div>", "<div></div><div></div><div><div></div></div><div></div>", "<div></div><div></div><div></div><div><div></div></div>", "<div></div><div></div><div></div><div></div><div></div>"
  ]

  print(len(correct_5))

  missing = [tag for tag in correct_5 if tag not in mine[0]]

  print(missing)