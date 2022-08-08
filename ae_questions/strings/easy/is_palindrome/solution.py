"""
Write a function that takes a string and returns a boolean value indicating whether or not that string is a palindrome.
"""
def is_palindrome(string):
  return string[::-1] == string


if __name__ == "__main__":
  print(is_palindrome('wow'))