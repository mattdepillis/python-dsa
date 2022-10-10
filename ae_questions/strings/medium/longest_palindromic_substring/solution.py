"""
Write a function that returns the longest palindromic substring fed to it.

TC: O(n^2)
SC: O(n) -- worst-case must store n characters in string ```longest```.
"""
def longest_palindromic_substring(string):
  longest = ""
  for i in range(len(string)):
    for j in range(i, -1, -1):
      s = string[j : i + 1]
      if s == s[::-1] and len(s) > len(longest):
        longest = s
  return longest


if __name__ == "__main__":
  print(longest_palindromic_substring("abaxyzzyxf"))