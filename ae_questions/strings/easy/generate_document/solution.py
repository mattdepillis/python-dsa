"""
Given a string of available characters to use (case sensitive + special characters), and a string (document) you want to generate from the available characters, write a function that returns a boolean indicating whether or not you were able to do so.
"""
def generate_document(chars, document):
  char_bank = {}
  for char in chars:
    if char not in char_bank:
      char_bank[char] = 0
    char_bank[char] += 1
  
  for c in document:
    if c not in char_bank or char_bank[c] == 0:
      return False
    char_bank[c] -= 1
  
  return True


if __name__ == "__main__":
  print(generate_document('aheaollabbb sjfkd s', 'hello'))