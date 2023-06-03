"""

"""
def one_edit(s1, s2):
  if abs(len(s1) - len(s2)) > 1: return False

  i = edits = 0
  insert = len(s1) != len(s2)
  longer, shorter = (s1, s2) if len(s1) >= len(s2) else (s2, s1)

  while i < len(shorter):
    j = i + edits if insert else i    
    if shorter[i] != longer[j]:
      edits += 1
      if edits > 1: return False
      if not insert: i += 1
    else: i += 1

  return True


if __name__ == "__main__":
  print(one_edit(
    "hello",
    "hallo"
  ))

  print(one_edit(
    "abcdefg",
    "abdefg"
  ))

  print(one_edit(
    "bb",
    "a"
  ))