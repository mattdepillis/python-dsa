"""
Write a function that takes an array of words and returns the minimum number of characters needed to form all of the words.

TC: O(n * m) -- where n = the number of words and m = length of the longest word
SC: O(c) -- where c = the number of unique characters in the string
"""
def min_characters_for_words(words):
  chars, l = {}, []
  for word in words:
    multiple = {}
    for letter in word:
      if letter not in chars:
        chars[letter] = multiple[letter] = 1
      else:
        if letter not in multiple: multiple[letter] = 1
        else: multiple[letter] += 1
    for key in multiple:
      if multiple[key] > chars[key]: chars[key] = multiple[key]

  for letter in chars:
    for _ in range(chars[letter]):
      l.append(letter)

  return l



if __name__ == "__main__":
  print(min_characters_for_words(
    ["this", "that", "did", "deed", "them!", "a"]
  ))
  # ["!", "a", "d", "d", "e", "e", "h", "i", "m", "s", "t", "t"]
  # ['!', 'a', 'd', 'd', 'd', 'e', 'e', 'h', 'i', 'm', 's', 't', 't']