"""
Write a function that takes a string and an integer key and returns the string shifted in Caesar's Cipher method by y spots equaling the value of the key.
"""

def caesars_cipher(string, key):
  encrypted = ""
  for letter in string:
    remainder = (ord(letter) + key - 97) % 26
    encrypted += chr(remainder + 97)
  return encrypted


if __name__ == "__main__":
  print(caesars_cipher('azyx', 1))