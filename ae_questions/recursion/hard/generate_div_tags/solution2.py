"""

"""
def recurse(opening, closing, prefix, combos):
  if opening > 0:
    p = prefix + "<div>"
    print('opening', p)
    recurse(opening - 1, closing, p, combos)
  if opening < closing:
    p = prefix + "</div>"
    print('closing', p)
    recurse(opening, closing - 1, p, combos)
  
  if closing == 0:
    print('prefix', prefix)
    combos.append(prefix)

def generate_div_tags(tags):
  valid = []
  recurse(tags, tags, "", valid)
  return valid


if __name__ == "__main__":
  v = generate_div_tags(5)
  print(len(v))