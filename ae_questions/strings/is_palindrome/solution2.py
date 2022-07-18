"""
Write a function that takes a string and returns a boolean value indicating whether or not that string is a palindrome.
(This solution includes conversion of all chars to lowercase + removes non-alphanumeric chars).
"""
import re

def is_palindrome(string):
  string = re.sub(r'\W+', '', string).lower()
  return string[::-1] == string


if __name__ == "__main__":
  print(is_palindrome('wow...'))